import random
import weapon
import pygame
import scene
import dinosaur
import obstacle
import setup

# pygame setup
pygame.init()
back_ground = scene.Ground()
dino = dinosaur.Dino()
laser = weapon.Laser()
blade = weapon.Blade()
cacti = pygame.sprite.Group()
scoreboard = scene.Scoreboard()
pterodactyls = pygame.sprite.Group()


screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
spawn_rate_cacti = 0
spawn_time_cacti = 0
spawn_rate_pter = 0
spawn_time_pter = 0
# create a ground image
back_ground.load()
dino.load()
dino.run()

# game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino.state == 'run':
                dino.jump()
            if event.key == pygame.K_RIGHT and dino.state == 'run':
                dino.dash()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and dino.state == 'run':
                dino.duck()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN and dino.state == 'duck':
                dino.run()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                laser.active()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                blade.active()


    if spawn_time_cacti == spawn_rate_cacti:
        cacti.add(obstacle.Cactus())
        spawn_rate_cacti = random.randint(80, 300)
        spawn_time_cacti = 0
    if spawn_rate_pter == spawn_time_pter:
        pterodactyls.add(obstacle.Pterodactyl(random.randint(200, 400)))
        spawn_rate_pter = random.randint(400, 800)
        spawn_time_pter = 0

    spawn_time_cacti += 1
    spawn_time_pter += 1

    for cactus in cacti:
        if pygame.sprite.collide_mask(laser, cactus) and laser.state == 'active':
            cactus.knock_up()

        if pygame.sprite.collide_mask(dino, cactus):
            if dino.state != 'dash':
                dino.die()
                running = False
            else:
                cactus.knock()

    for pterodactyl in pterodactyls:
        if pygame.sprite.collide_mask(laser, pterodactyl) and laser.state == 'active':
            pterodactyl.knock_up()

        if pygame.sprite.collide_mask(dino, pterodactyl):
            if dino.state != 'dash':
                dino.die()
                running = False
            else:
                pterodactyl.knock()

    screen.fill("White")

    # fill the screen with a color to wipe away anything from last frame
    back_ground.update()
    dino.update()
    cacti.update()
    scoreboard.update()
    laser.update()
    blade.update()
    pterodactyls.update()
    scoreboard.get_score(back_ground)
    scoreboard.draw(screen)
    pterodactyls.draw(screen)
    laser.draw(screen)
    cacti.draw(screen)
    blade.draw(screen)
    back_ground.draw(screen)
    dino.draw(screen)
    pygame.display.flip()

    clock.tick(setup.FPS_limit)


pygame.quit()