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
cacti = pygame.sprite.Group()
scoreboard = scene.Scoreboard()
pterodactyls = pygame.sprite.Group()
beam = weapon.Beam()
shield = weapon.Shield()

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
            if event.key == pygame.K_DOWN and dino.state == 'run':
                dino.duck()
            if event.key == pygame.K_UP and laser.state == 'inactive' and back_ground.score >= 1000:
                back_ground.score -= 1000
                laser.active(dino.get_rect())
            if event.key == pygame.K_LEFT and beam.state == 'inactive' and back_ground.score >= 2000:
                back_ground.score -= 2000
                beam.active(dino.get_rect())
            if event.key == pygame.K_RCTRL and shield.state == 'inactive' and back_ground.score >= 2500:
                back_ground.score -= 2500
                shield.active()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN and   dino.state == 'duck':
                dino.run()

    if spawn_time_cacti == spawn_rate_cacti:
        cacti.add(obstacle.Cactus())
        spawn_rate_cacti = random.randint(200, 500)
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
        if pygame.sprite.collide_mask(cactus, beam) and beam.state == 'active':
            cactus.destroy()
        if pygame.sprite.collide_mask(cactus, shield) and shield.state == 'active':
            cactus.destroy()
            shield.inactive()

    for pterodactyl in pterodactyls:
        if pygame.sprite.collide_mask(laser, pterodactyl) and laser.state == 'active':
            pterodactyl.knock_up()

        if pygame.sprite.collide_mask(dino, pterodactyl):
            if dino.state != 'dash':
                dino.die()
                running = False
            else:
                pterodactyl.knock()
        if pygame.sprite.collide_mask(pterodactyl, beam) and beam.state == 'active':
            pterodactyl.destroy()
        if pygame.sprite.collide_mask(pterodactyl, shield) and shield.state == 'active':
            pterodactyl.destroy()
            shield.inactive()

    screen.fill("White")
    back_ground.score = 20000
    # fill the screen with a color to wipe away anything from last frame
    back_ground.update()
    dino.update()
    cacti.update()
    scoreboard.update()
    laser.update()
    pterodactyls.update()
    beam.update()
    shield.update(dino.get_rect())

    scoreboard.get_score(back_ground)
    scoreboard.draw(screen)
    pterodactyls.draw(screen)
    laser.draw(screen)
    beam.draw(screen)
    cacti.draw(screen)
    back_ground.draw(screen)
    dino.draw(screen)
    shield.draw(screen)
    pygame.display.flip()

    clock.tick(setup.FPS_limit)


pygame.quit()