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

    def active(self):
        self.state = 'active'


class Blade(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.state = 'inactive'
        self.angle = 0
        self.image_addr = setup.Image_addr_laser
        self.image = pygame.image.load(self.image_addr)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.bottom = setup.dino_pos + 5, setup.dino_height + 40

    def update(self):
        if self.state == 'active':
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.mask = pygame.mask.from_surface(self.image)
            self.angle += 1
            if self.angle == 10:
                self.image = pygame.transform.rotate(self.image, 0)
                self.rect = self.image.get_rect(center=self.rect.center)
                self.mask = pygame.mask.from_surface(self.image)
                self.state = 'inactive'
                self.angle = 0
                self.kill()
        if self.rect.left > 1280:
            self.rect.left = setup.dino_pos + 5
            self.state = 'inactive'

    def disable(self):
        self.state = "inactive"
        self.rect.left = setup.dino_pos + 5

    def draw(self, screen):
        if self.state == 'active':
            screen.blit(self.image, self.rect)

    def active(self):
        self.state = 'active'
