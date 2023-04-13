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

    # draw
    screen.fill(BACKGROUND)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    # pg.display.flip()

pg.quit()
