import pygame as pg
import numpy as np
from math import cos, sin, radians

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Catppuccin Mocha colorscheme
BACKGROUND = (18, 18, 25)
COLORS = [(166, 227, 161), (245, 194, 231), (116, 199, 236), (249, 226, 175), (180, 190, 254),
          (137, 220, 235), (203, 166, 247), (243, 139, 168), (250, 179, 135), (137, 180, 250)]
cubes = []


def projection_matrix(z):
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 1/z, 0]])


def translation_matrix(dx, dy, dz):
    return np.array([[1, 0, 0, dx],
                     [0, 1, 0, dy],
                     [0, 0, 1, dz],
                     [0, 0, 0, 1]])


def rot_mat_x(a):  # tilt
    a = radians(a)
    return np.array([[1,      0,       0, 0],
                     [0, cos(a), -sin(a), 0],
                     [0, sin(a),  cos(a), 0],
                     [0,      0,       0, 1]])


def rot_mat_y(a):  # pan
    a = radians(a)
    return np.array([[cos(a), 0, sin(a), 0],
                     [0, 1,      0, 0],
                     [-sin(a), 0, cos(a), 0],
                     [0, 0,      0,  1]])


def rot_mat_z(a):  # roll
    a = radians(a)
    return np.array([[cos(a), -sin(a), 0, 0],
                     [sin(a), cos(a), 0, 0],
                     [0,      0, 1, 0],
                     [0,      0, 0, 1]])


def translate(dx, dy, dz):
    for cube in cubes:
        for i in range(len(cube)):
            vertex = cube[i]
            cube[i] = tuple(np.matmul(translation_matrix(dx, dy, dz), vertex))


def tilt(a):
    for cube in cubes:
        for i in range(len(cube)):
            vertex = cube[i]
            cube[i] = tuple(np.matmul(rot_mat_x(a), vertex))


def pan(a):
    for cube in cubes:
        for i in range(len(cube)):
            vertex = cube[i]
            cube[i] = tuple(np.matmul(rot_mat_y(a), vertex))


def roll(a):
    for cube in cubes:
        for i in range(len(cube)):
            vertex = cube[i]
            cube[i] = tuple(np.matmul(rot_mat_z(a), vertex))


def projection_normalization(vtx):
    if vtx[3] == 0:
        print("dzielenie przez 0")
    return [vtx[0]/vtx[3], vtx[1]/vtx[3], vtx[2]/vtx[3], 1]
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
    cubes.append(create_cube(0, 0, 175, 50))
    cubes.append(create_cube(0, -75, 175, 50))
    cubes.append(create_cube(-75, 0, 175, 50))
    cubes.append(create_cube(-75, -75, 175, 50))


def draw_cube_edges(cube, color):
    if (cube[0][2] > 0 and cube[1][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[0]), translate_for_display(cube[1]))
    if (cube[0][2] > 0 and cube[2][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[0]), translate_for_display(cube[2]))
    if (cube[1][2] > 0 and cube[3][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[1]), translate_for_display(cube[3]))
    if (cube[2][2] > 0 and cube[3][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[2]), translate_for_display(cube[3]))

    if (cube[4][2] > 0 and cube[5][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[4]), translate_for_display(cube[5]))
    if (cube[4][2] > 0 and cube[6][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[4]), translate_for_display(cube[6]))
    if (cube[5][2] > 0 and cube[7][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[5]), translate_for_display(cube[7]))
    if (cube[6][2] > 0 and cube[7][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[6]), translate_for_display(cube[7]))

    if (cube[0][2] > 0 and cube[4][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[0]), translate_for_display(cube[4]))
    if (cube[1][2] > 0 and cube[5][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[1]), translate_for_display(cube[5]))
    if (cube[2][2] > 0 and cube[6][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[2]), translate_for_display(cube[6]))
    if (cube[3][2] > 0 and cube[7][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(
            cube[3]), translate_for_display(cube[7]))


def draw_cube(cube, color):
    cube_projection = []
    for vertex in cube:
        visible = True if vertex[2] > 0 else False
        v_p = np.matmul(projection_matrix(z), vertex)
        v_p = projection_normalization(v_p)
        v_p[2] = 1 if visible else 0
        cube_projection.append(tuple(v_p))
    draw_cube_edges(cube_projection, color)


pg.init()
pg.display.set_caption("Virtual Camera")
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
init_cubes()

# clock = pg.time.Clock()
z = 200
font = pg.font.SysFont("Arial", 36)

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
        tilt(0.1)
    if keys[pg.K_k] == True:  # K -> Tilt Up
        tilt(-0.1)
    if keys[pg.K_j] == True:  # J -> Pan Left
        pan(0.1)
    if keys[pg.K_l] == True:  # L -> Pan Right
        pan(-0.1)
    if keys[pg.K_u] == True:  # U -> Roll Left
        roll(-0.1)
    if keys[pg.K_o] == True:  # O -> Roll Right
        roll(0.1)

    if keys[pg.K_w] == True:  # W -> Zoom Out
        if z > 100:
            z -= 0.5
    if keys[pg.K_r] == True:  # R -> Zoom In
        if z < 400:
            z += 0.5

    # draw
    screen.fill(BACKGROUND)
    for i, cube in enumerate(cubes):
        draw_cube(cubes[i], COLORS[i % len(COLORS)])
        # draw_cube(cubes[i], random.choice(COLORS)) disco

    zoom = font.render(f"Zoom: {round(z/200*100, 1)}%", True, COLORS[4])
    screen.blit(zoom, (10, 10))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    # pg.display.flip()

pg.quit()
