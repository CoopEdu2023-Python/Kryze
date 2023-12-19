import pygame
import setup


class Ground:

    def __init__(self):
        self.image_addr = setup.Image_addr_background
        self.rect = pygame.rect.Rect
        self.rect_next = pygame.rect.Rect
        self.image = pygame.surface.Surface
        self.image_next = pygame.surface.Surface
        self.score = 0

    def load(self):
        self.image = pygame.image.load(self.image_addr)
        self.image_next = self.image
        self.rect = self.image.get_rect()
        self.rect_next = self.image_next.get_rect()
        self.rect.left, self.rect.bottom = 0, setup.Ground_height
        self.rect_next.left = self.rect.width
        self.rect_next.bottom = setup.Ground_height

    def update(self):
        self.rect.left -= setup.Going_speed
        self.score += setup.Going_speed // 5
        self.rect_next.left -= setup.Going_speed
        if self.rect.right <= 0:
            self.rect.left = self.rect_next.right
        if self.rect_next.right <= 0:
            self.rect_next.left = self.rect.right

    def draw(self, background):
        background.blit(self.image, self.rect)
        background.blit(self.image_next, self.rect_next)


class Moon:
    pass


class Cloud:
    pass


class Star:
    pass


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.image_addr = setup.Image_addr_scoreboard
        self.images = []
        for addr in self.image_addr:
            self.images.append(pygame.image.load(addr))
        # print(len(self.images))
        self.image_score = pygame.Surface((20 * 5, 21))
        self.rect = self.image_score.get_rect()
        self.rect.left, self.rect.bottom = 1100, 40

    def get_score(self, ground):
        self.score = ground.score // 10
        # print(self.score)
        if self.score and not self.score % 100:
            pygame.mixer.Sound('resources/audios/score.mp3').play()

    def update(self):
        if self.score >= 0:
            self.image_score.fill('white')
            score_str = '0' * (5 - len(str(self.score))) + str(self.score)
            # add image to scoreboard
            # print(score_str)
            for i in range(5):
                self.image_score.blit(self.images[int(score_str[i])], (20 * i, 0))
            self.image_score.set_alpha(255)

    def draw(self, screen):
        screen.blit(self.image_score, self.rect)


class EndingIcon:
    pass
