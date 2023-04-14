import pygame as pg
from matrices import *

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

cubes = []
screen_width = 0
screen_height = 0


def init_screen(w, h):
    global screen_width, screen_height
    screen_width = w
    screen_height = h


def init_cubes():
    cubes.append(create_cube(0, 0, 100, 50))
    cubes.append(create_cube(0, -75, 100, 50))
    cubes.append(create_cube(-75, 0, 100, 50))
    cubes.append(create_cube(-75, -75, 100, 50))
    cubes.append(create_cube(0, 0, 175, 50))
    cubes.append(create_cube(0, -75, 175, 50))
    cubes.append(create_cube(-75, 0, 175, 50))
    cubes.append(create_cube(-75, -75, 175, 50))


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


def draw_cube(screen, cube, color, z):
    cube_projection = []
    for vertex in cube:
        visible = True if vertex[2] > 0 else False

        v_p = np.matmul(projection_matrix(z), vertex)
        v_p = projection_normalization(v_p)
        v_p[2] = 1 if visible else 0

        cube_projection.append(tuple(v_p))
    draw_cube_edges(screen, cube_projection, color)


def draw_cube_edges(screen, cube, color):
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


def projection_normalization(vtx):
    return [vtx[0]/vtx[3], vtx[1]/vtx[3], vtx[2]/vtx[3], 1]


def translate_for_display(coords):
    return (screen_width/2 + coords[0], screen_height/2 - coords[1])


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
