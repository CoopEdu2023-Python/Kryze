import pygame
import setup


class Dino(pygame.sprite.Sprite):

    def calculate_jump_height_per_frame(self, frame_count, frame_time_interval):
        velocity_start = 17
        g = 50
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
        self.image_id = 0
        self.image_addr_list_run = setup.Image_addr_dino_run_list
        self.image_addr_list_jump = setup.Image_addr_dino_jump_list
        self.image_addr_list_duck = setup.Image_addr_dino_duck_list
        self.image_addr_list_die = setup.Image_addr_dino_die_list
        self.rect = pygame.rect.Rect
        self.image_current = pygame.surface.Surface
        self.image_current_list = []
        self.image_run_list = []
        self.image_jump_list = []
        self.image_duck_list = []
        self.image_die_list = []
        self.refresh_rate = setup.FPS_limit // 20
        self.refresh_time = 0
        self.state = "run"
        self.jump_time = 0
        self.mask = None
        self.jump_height = self.calculate_jump_height_per_frame(setup.FPS_limit, 2 / setup.FPS_limit)
        print(self.jump_height)

    def load(self):
        for addr in self.image_addr_list_run:
            self.image_run_list.append(pygame.image.load(addr))
        for addr in self.image_addr_list_jump:
            self.image_jump_list.append(pygame.image.load(addr))
        for addr in self.image_addr_list_duck:
            self.image_duck_list.append(pygame.image.load(addr))
        for addr in self.image_addr_list_die:
            self.image_die_list.append(pygame.image.load(addr))
        self.image_current = self.image_run_list[0]
        self.rect = self.image_current.get_rect()
        self.rect.left, self.rect.bottom = setup.dino_pos, setup.dino_height
        self.mask = pygame.mask.from_surface(self.image_current)

    def die(self):
        self.state = "die"
        self.refresh_time = 0
        self.image_id = 0
        self.image_current_list.clear()
        self.image_current_list.extend(self.image_die_list)

    def run(self):
        self.state = "run"
        self.refresh_time = 0
        self.image_id = 0
        self.image_current_list.clear()
        self.image_current_list.extend(self.image_run_list)

    def duck(self):
        self.state = "duck"
        self.refresh_time = 0
        self.image_id = 0
        self.image_current_list.clear()
        self.image_current_list.extend(self.image_duck_list)

    def dash(self):
        self.state = "dash"
        self.refresh_time = 0
        self.image_current_list.clear()
        self.image_current_list.extend(self.image_run_list)

    def jump(self):
        pygame.mixer.Sound(setup.Jump_sound).play()
        self.refresh_time = 0
        self.state = "jump"
        self.image_id = 0
        self.image_current_list.clear()
        self.image_current_list.extend(self.image_jump_list)

    def switch_image(self):
        if self.image_id == len(self.image_current_list):
            self.image_id = 0
        self.image_current = self.image_current_list[self.image_id]
        self.image_id += 1
        self.mask = pygame.mask.from_surface(self.image_current)

    def update(self):
        if self.state == 'run' or 'duck':
            if self.refresh_time == self.refresh_rate:
                self.switch_image()
                self.refresh_time = 0
            else:
                self.refresh_time += 1
        if self.state == 'jump':
            self.rect.bottom -= self.jump_height[self.jump_time]
            self.switch_image()
            self.jump_time += 1
            if self.jump_time == len(self.jump_height):
                self.run()
                self.rect.bottom = setup.dino_height
                self.jump_time = 0
        if self.state == "dash":
            self.rect.left += self.jump_height[self.jump_time]
            self.switch_image()
            self.jump_time += 1
            if self.jump_time == len(self.jump_height):
                self.run()
                self.rect.left = setup.dino_pos
                self.jump_time = 0

    def draw(self, background):
        background.blit(self.image_current, self.rect)



