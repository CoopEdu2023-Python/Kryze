import pygame
import setup


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.state = 'inactive'
        self.image_addr = setup.Image_addr_laser
        self.image = pygame.image.load(self.image_addr)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = setup.dino_pos + 5, setup.dino_height + 40
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.state == 'active':
            self.rect.left += setup.Going_speed
            self.mask = pygame.mask.from_surface(self.image)
        if self.rect.left > 1280:
            self.rect.left = setup.dino_pos + 5
            self.state = 'inactive'

    def disable(self):
        self.state = "inactive"
        self.rect.left = setup.dino_pos + 5

    def draw(self, screen):
        if self.state == 'active':
            screen.blit(self.image, self.rect)

    def active(self, pos):
        self.state = 'active'
        self.rect.left = pos.left + 5
        self.rect.bottom = pos.bottom + 40


class Beam(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_addr = setup.Image_addr_beam
        self.image_per = pygame.image.load(self.image_addr)
        self.parts = []
        self.rect = self.image_per.get_rect()
        self.state = 'inactive'
        self.rects = []
        self.generate_rate = 5
        self.generate_time = 0
        self.image = self.image_per

    def active(self, pos):
        self.state = 'active'
        self.parts.append(self.image_per)
        rect_first = self.image_per.get_rect()
        rect_first.left, rect_first.bottom = pos.left + 90, pos.bottom - 30
        self.rects.append(rect_first)
        self.rect = self.rects[-1]

    def inactive(self):
        self.state = 'inactive'
        self.parts.clear()
        self.rects.clear()
        self.parts.append(self.image_per)
        rect_first = self.image_per.get_rect()
        rect_first.left, rect_first.bottom = setup.dino_pos + 90, setup.dino_height - 30
        self.rects.append(rect_first)

    def update(self):
        if self.state == 'active':
            if self.rects[-1].right <= 1280 and self.generate_rate == self.generate_time:
                _ = self.image_per.get_rect()
                _.left, _.bottom = self.rects[-1].right, self.rects[-1].bottom
                self.rects.append(_)
                self.parts.append(self.image_per)
                self.rect = self.rects[-1]
                self.mask = pygame.mask.from_surface(self.parts[-1])
                self.generate_time = 0
            self.generate_time += 1
            if self.rects[-1].right >= 1280:
                self.inactive()
                self.generate_time = 0

    def draw(self, screen):
        if self.state == 'active':
            for part in range(1, len(self.rects)):
                screen.blit(self.parts[part], self.rects[part])


class Shield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(setup.Image_addr_shield)
        self.rect = self.image.get_rect()
        self.state = 'inactive'
        self.mask = pygame.mask.from_surface(self.image)

    def active(self):
        self.state = 'active'

    def inactive(self):
        self.state = 'inactive'

    def update(self, pos: pygame.rect.Rect):
        self.rect.left = pos.left - 100
        self.rect.bottom = pos.bottom + 80
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        if self.state == 'active':
            screen.blit(self.image, self.rect)


