import pygame
import scene
import dinosaur
import setup


# pygame setup
pygame.init()
back_ground = scene.Ground()
dino = dinosaur.Dino()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# create a ground image
back_ground.load()
dino.load()
dino.run()

# game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            dino.jump()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and dino.state == 'run':
                dino.duck()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN and dino.state == 'duck':
                dino.run()

    # fill the screen with a color to wipe away anything from last frame
    back_ground.update()
    dino.update()
    back_ground.draw(screen)
    dino.draw(screen)
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(setup.FPS_limit)

pygame.quit()