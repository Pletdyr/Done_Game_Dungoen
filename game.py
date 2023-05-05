import pygame as pg
import random
import time
from classes import Tahm, Monster

## Screen setup ##
pg.init()
w = 1000
h = 500
screen = pg.display.set_mode((w,h))
pg.display.set_caption("Cracked spil")

## Level ##
game_map = pg.image.load("gamemap.png").convert_alpha()
game_map = pg.transform.scale(game_map, (w, h)) 
x = (w - game_map.get_width()) // 2
y = (h - game_map.get_height()) // 2

## Game Loop ##
tahm = Tahm(50, 50)
monsters = [Monster(900, 50, tahm), Monster(800, 150, tahm), Monster(700, 250, tahm),]

player_direction = False
running = True
tick = 0
start_time = time.time()

font = pg.font.SysFont(None, 36)
timer_start = time.time()

while running:

    # Event loop
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            player_direction = "left"
        elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            player_direction = "right"
        elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
            player_direction = "up"
        elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            player_direction = "down"

        if event.type == pg.KEYUP and event.key == pg.K_LEFT:
            player_direction = False
        elif event.type == pg.KEYUP and event.key == pg.K_RIGHT:
            player_direction = False
        elif event.type == pg.KEYUP and event.key == pg.K_UP:
            player_direction = False
        elif event.type == pg.KEYUP and event.key == pg.K_DOWN:
            player_direction = False

    # Draw level #
    screen.fill((0,0,0))
    screen.blit(game_map, (x,y))

    # Draw characters #
    tahm.draw(screen)
    for monster in monsters:
        monster.draw(screen)

    if tahm.health == 0:
        game_map = pg.image.load("deathscreen.png").convert_alpha()
        game_map = pg.transform.scale(game_map, (w, h))
        x = (w - game_map.get_width()) // 2
        y = (h - game_map.get_height()) // 2
        screen.blit(game_map, (x, y))
        pg.display.update()
        time.sleep(2)
        running = False

    # Logic
    tahm.update(player_direction, game_map, monsters)
    for monster in monsters:
        monster.update()

    if time.time() - timer_start >= 30:
        game_map = pg.image.load("youwin.png").convert_alpha()
        game_map = pg.transform.scale(game_map, (w, h))
        x = (w - game_map.get_width()) // 2
        y = (h - game_map.get_height()) // 2
        screen.blit(game_map, (x, y))
        pg.display.update()
        time.sleep(2)
        running = False
    
    # Timer
    elapsed_time = int(time.time() - timer_start)
    timer_text = font.render(f"Tid: {elapsed_time}", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

    # Update screen
    pg.display.flip()

    # Framerate
    tick += 1
    time.sleep(0.02)