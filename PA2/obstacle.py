import random
import pygame
import setup


class Cactus(pygame.sprite.Sprite):
    def calculate_jump_height_per_frame(self, frame_count, frame_time_interval):
        velocity_start = 17
        g = 40
        jump_heights = []
        for frame in range(1, frame_count + 1):
            total_time = frame * frame_time_interval
            jump_height = velocity_start - g * total_time
            jump_heights.append(jump_height)
            if jump_height < 0:
                break
        for i in range(len(jump_heights) - 1, 0, -1):
            jump_heights.append(-1 * jump_heights[i])
        return jump_heights

    def __init__(self):
        super().__init__()
        self.state = "normal"
        self.jump_time = 0
        self.image_addr = setup.Image_addr_cactus
        self.image = pygame.image.load(random.choice(self.image_addr))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = 1280, setup.Ground_height - 8
        self.mask = pygame.mask.from_surface(self.image)
        self.jump_height = self.calculate_jump_height_per_frame(setup.FPS_limit, 2 / setup.FPS_limit)

    def update(self):
        if self.state == 'normal':
            self.rect.left -= setup.Going_speed
            if self.rect.right < 0:
                self.kill()
        if self.state == 'knocked':
            self.rect.left += setup.Going_speed
            self.rect.bottom -= self.jump_height[self.jump_time]
            self.jump_time += 1
            if self.jump_time == len(self.jump_height):
                self.state = 'normal'
                self.rect.bottom = setup.dino_height
                self.jump_time = 0
        if self.state == "knocked_up":
            self.rect.left += setup.Going_speed
            self.rect.bottom -= self.jump_height[self.jump_time]
            self.jump_time += 1
            if self.jump_time == len(self.jump_height) // 2:
                self.state = 'normal'
                self.jump_time = 0
                self.kill()

    def knock(self):
        self.state = "knocked"

    def knock_up(self):
        self.state = 'knocked_up'

    def draw(self, background):
        background.blit(self.image, self.rect)


class Pterodactyl:
    pass

