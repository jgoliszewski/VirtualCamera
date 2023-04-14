import random
import pygame as pg
import numpy as np

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Catppuccin Mocha colorscheme
BACKGROUND = (18, 18, 25)
COLORS = [(245, 194, 231), (203, 166, 247), (243, 139, 168), (250, 179, 135), (249, 226, 175),
          (166, 227, 161), (137, 220, 235), (116, 199, 236), (137, 180, 250), (180, 190, 254)]
cubes = []


def projection_matrix():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0.01, 0]])


def translation_matrix(dx, dy, dz):
    return np.array([[1, 0, 0, dx],
                     [0, 1, 0, dy],
                     [0, 0, 1, dz],
                     [0, 0, 0, 1]])


def translate(dx, dy, dz):
    for cube in cubes:
        for i in range(len(cube)):
            vertex = cube[i]
            cube[i] = tuple(np.matmul(translation_matrix(dx, dy, dz), vertex))


def projection_normalization(vtx):
    if vtx[3] == 0:
        print("dzielenie przez 0")
    return (vtx[0]/vtx[3], vtx[1]/vtx[3], vtx[2]/vtx[3], 1)
    # return (vtx[0]/1, vtx[1]/1, vtx[2]/1, 1)


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
    cubes.append(create_cube(0, 0, 100, 50))
    cubes.append(create_cube(0, -75, 100, 50))
    cubes.append(create_cube(-75, 0, 100, 50))
    cubes.append(create_cube(-75, -75, 100, 50))


def draw_cube_edges(cube, color):
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


def draw_cube(cube, color):
    cube_projection = []
    for vertex in cube:
        v_p = np.matmul(projection_matrix(), vertex)
        v_p = projection_normalization(v_p)
        cube_projection.append(v_p)
    draw_cube_edges(cube_projection, color)


pg.init()
pg.display.set_caption("Virtual Camera")
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
init_cubes()

# clock = pg.time.Clock()

run = True
while run:
    # clock.tick(60)

    # controls
    keys = pg.key.get_pressed()

    if keys[pg.K_e] == True:  # E -> Move Forward
        translate(0, 0, -0.2)
    if keys[pg.K_d] == True:  # D -> Move Back
        translate(0, 0, 0.2)
    if keys[pg.K_s] == True:  # S -> Move Left
        translate(0.2, 0, 0)
    if keys[pg.K_f] == True:  # F -> Move Right
        translate(-0.2, 0, 0)
    if keys[pg.K_g] == True:  # G -> Move Down
        translate(0, 0.2, 0)
    if keys[pg.K_t] == True:  # T -> Move Up
        translate(0, -0.2, 0)

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
        draw_cube(cubes[i], COLORS[i % len(COLORS)])
        # draw_cube(cubes[i], random.choice(COLORS)) disco

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    # pg.display.flip()

pg.quit()
