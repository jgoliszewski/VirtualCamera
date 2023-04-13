import pygame as pg

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Catppuccin Mocha colorscheme
BACKGROUND = (18, 18, 25)


pg.init()
pg.display.set_caption("Virtual Camera")
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
run = True

while run:
    # clock.tick(60)

    # controls
    keys = pg.key.get_pressed()

    if keys[pg.K_e] == True:  # E -> Move Forward
        print("Move Forward")
    if keys[pg.K_d] == True:  # D -> Move Back
        print("Move Back")
    if keys[pg.K_s] == True:  # S -> Move Left
        print("Move Left")
    if keys[pg.K_f] == True:  # F -> Move Right
        print("Move Right")
    if keys[pg.K_t] == True:  # R -> Move Up
        print("Move Up")
    if keys[pg.K_g] == True:  # W -> Move Down
        print("Move Down")

    if keys[pg.K_i] == True:  # I -> Tilt Down
        print("Tilt Down")
    if keys[pg.K_k] == True:  # K -> Tilt Up
        print("Tilt Up")
    if keys[pg.K_j] == True:  # J -> Pan Left
        print("Pan Left")
    if keys[pg.K_l] == True:  # L -> Pan Right
        print("Pan Right")
    if keys[pg.K_u] == True:  # U -> Roll Left
        print("Roll Left")
    if keys[pg.K_o] == True:  # O -> Roll Right
        print("Rol Right")

    if keys[pg.K_w] == True:  # W -> Zoom Out
        print("Zoom out")
    if keys[pg.K_r] == True:  # R -> Zoom In
        print("Zoom in")

    # draw
    screen.fill(BACKGROUND)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    # pg.display.flip()

pg.quit()
