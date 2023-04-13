import random
import pygame as pg

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Catppuccin Mocha colorscheme
BACKGROUND = (18, 18, 25)
COLORS = [(245, 194, 231), (203, 166, 247), (243, 139, 168), (250, 179, 135), (249, 226, 175),
          (166, 227, 161), (137, 220, 235), (116, 199, 236), (137, 180, 250), (180, 190, 254)]
cubes = []


def create_cube(x, y, z, size):
    points = []
    points.append((x, y, z, 1))
    points.append((x+size, y, z, 1))
    points.append((x, y+size, z, 1))
    points.append((x+size, y+size, z, 1))

    points.append((x, y, z+size, 1))
    points.append((x+size, y, z+size, 1))
    points.append((x, y+size, z+size, 1))
    points.append((x+size, y+size, z+size, 1))
    return points


def init_cubes():
    global cubes
    cubes.append(create_cube(0, 0, 0, 50))
    cubes.append(create_cube(0, 75, 0, 50))


def translate_for_display(coords):
    return (SCREEN_WIDTH/2 + coords[0], SCREEN_HEIGHT/2 - coords[1])

# Cube Vertices
#    6--------7
#   /|       /|
#  / |      / |
# 4--------5  |
# |  |     |  |
# |  2-----|--3
# | /      | /
# |/       |/
# 0--------1


def draw_cube(cube, color):
    pg.draw.aaline(screen, color, translate_for_display(
        cube[0]), translate_for_display(cube[1]))
    pg.draw.aaline(screen, color, translate_for_display(
        cube[0]), translate_for_display(cube[2]))
    pg.draw.aaline(screen, color, translate_for_display(
        cube[1]), translate_for_display(cube[3]))
    pg.draw.aaline(screen, color, translate_for_display(
        cube[2]), translate_for_display(cube[3]))

    pg.draw.aaline(screen, color, translate_for_display(
        cube[4]), translate_for_display(cube[5]))
    pg.draw.aaline(screen, color, translate_for_display(
        cube[4]), translate_for_display(cube[6]))
    pg.draw.aaline(screen, color, translate_for_display(
        cube[5]), translate_for_display(cube[7]))
    pg.draw.aaline(screen, color, translate_for_display(
        cube[6]), translate_for_display(cube[7]))

    pg.draw.aaline(screen, color, translate_for_display(
        cube[0]), translate_for_display(cube[4]))
    pg.draw.aaline(screen, color, translate_for_display(
        cube[1]), translate_for_display(cube[5]))
    pg.draw.aaline(screen, color, translate_for_display(
        cube[2]), translate_for_display(cube[6]))
    pg.draw.aaline(screen, color, translate_for_display(
        cube[3]), translate_for_display(cube[7]))


pg.init()
pg.display.set_caption("Virtual Camera")
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
init_cubes()

clock = pg.time.Clock()

run = True
while run:
    clock.tick(60)

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
    for i, cube in enumerate(cubes):
        # draw_cube(cubes[i], random.choice(COLORS)) disco
        draw_cube(cubes[i], COLORS[i % len(COLORS)])

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    # pg.display.flip()

pg.quit()
