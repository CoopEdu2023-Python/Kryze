import pygame
import scene
# pygame setup
pygame.init()
back_ground = scene.Ground()
back_ground.background = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# create a ground image
back_ground.image_addr = 'resources/images/ground/ground.png'
back_ground.load()
back_ground.rect = back_ground.image.get_rect()
back_ground.rect_next = back_ground.image_next.get_rect()
back_ground.rect.left, back_ground.rect.bottom = 0, 650
back_ground.rect_next.left = back_ground.rect.width
back_ground.rect_next.bottom = 650
# game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    back_ground.update()
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()