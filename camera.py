import pygame as pg
import numpy as np

from drawing import *
import drawing as d

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900
# SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 1080


# Catppuccin Mocha colorscheme
BACKGROUND = (18, 18, 25)
COLORS = [(166, 227, 161), (245, 194, 231), (116, 199, 236), (249, 226, 175), (180, 190, 254),
          (137, 220, 235), (203, 166, 247), (243, 139, 168), (250, 179, 135), (137, 180, 250)]

pg.init()
pg.display.set_caption("Virtual Camera")
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
init_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
init_cubes()

z = 400
font = pg.font.SysFont("Arial", 30)

# clock = pg.time.Clock()
run = True
cooldown = 60
while run:
    # clock.tick(60)

    #! controls
    keys = pg.key.get_pressed()

    if keys[pg.K_e] == True:  # E -> Move Forward
        translate(0, 0, -0.5)
    if keys[pg.K_d] == True:  # D -> Move Back
        translate(0, 0, 0.5)
    if keys[pg.K_s] == True:  # S -> Move Left
        translate(0.5, 0, 0)
    if keys[pg.K_f] == True:  # F -> Move Right
        translate(-0.5, 0, 0)
    if keys[pg.K_g] == True:  # G -> Move Down
        translate(0, 0.5, 0)
    if keys[pg.K_t] == True:  # T -> Move Up
        translate(0, -0.5, 0)

    if keys[pg.K_i] == True:  # I -> Tilt Down
        tilt(0.3)
    if keys[pg.K_k] == True:  # K -> Tilt Up
        tilt(-0.3)
    if keys[pg.K_j] == True:  # J -> Pan Left
        pan(0.3)
    if keys[pg.K_l] == True:  # L -> Pan Right
        pan(-0.3)
    if keys[pg.K_u] == True:  # U -> Roll Left
        roll(-0.3)
    if keys[pg.K_o] == True:  # O -> Roll Right
        roll(0.3)

    if keys[pg.K_w] == True:  # W -> Zoom Out
        if z > 100:
            z -= 0.5
    if keys[pg.K_r] == True:  # R -> Zoom In
        if z < 400:
            z += 0.5

    if keys[pg.K_m] == True and cooldown == 0:
        change_mode()
        cooldown = 60
    if cooldown > 0:
        cooldown -= 1
    #! draw
    screen.fill(BACKGROUND)
    draw_cubes(screen, cubes, z);

    zoom = font.render(f"Zoom: {round(z/200*100, 1)}%", True, COLORS[4])
    screen.blit(zoom, (10, 10))
    mode = font.render(f"Fill walls: {d.mode}", True, COLORS[4])
    screen.blit(mode, (10, 50))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()

pg.quit()
