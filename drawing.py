import pygame as pg
from matrices import *
from objects import *
COLORS = [(166, 227, 161), (245, 194, 231), (116, 199, 236), (249, 226, 175), (180, 190, 254),
          (137, 220, 235), (203, 166, 247), (243, 139, 168), (250, 179, 135), (137, 180, 250)]
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
mode = False

def init_screen(w, h):
    global screen_width, screen_height
    screen_width = w
    screen_height = h

def change_mode():
    global mode
    mode = not mode

def init_cubes():
    cubes.append(create_cube(0, 0, 100, 50 , COLORS[0]))
    cubes.append(create_cube(0, -75, 100, 50, COLORS[1]))
    cubes.append(create_cube(-75, 0, 100, 50, COLORS[2]))
    cubes.append(create_cube(-75, -75, 100, 50, COLORS[3]))
    cubes.append(create_cube(0, 0, 175, 50, COLORS[4]))
    cubes.append(create_cube(0, -75, 175, 50, COLORS[5]))
    cubes.append(create_cube(-75, 0, 175, 50, COLORS[6]))
    cubes.append(create_cube(-75, -75, 175, 50, COLORS[7]))

def create_cube(x, y, z, size, color):
    vertices = []
    vertices.append(Vertex(x, y, z, 1))
    vertices.append(Vertex(x+size, y, z, 1))
    vertices.append(Vertex(x, y+size, z, 1))
    vertices.append(Vertex(x+size, y+size, z, 1))

    vertices.append(Vertex(x, y, z+size, 1))
    vertices.append(Vertex(x+size, y, z+size, 1))
    vertices.append(Vertex(x, y+size, z+size, 1))
    vertices.append(Vertex(x+size, y+size, z+size, 1))
    
    return Cube(vertices, color)

def draw_cubes(screen, cubes, z):
    walls = []
    for cube in cubes:
        for wall in cube_2_walls(cube):
            walls.append(wall)

    sort_walls(walls)

    for wall in walls:
        projected_wall = project_wall(wall, z)
        draw_wall(screen, projected_wall)

def sort_walls(walls):
    for i in range(len(walls)):
        for j in range(len(walls)):
            if walls[i] >= walls[j]:
                walls[i], walls[j] = walls[j], walls[i]
                

def project_wall(wall, z):
    wall_projection_vertecies = []
    for vertex in wall.vertecies:
        visible = True if vertex.z > 0 else False

        v_p = np.matmul(projection_matrix(z), vertex.get_tuple())
        v_p = projection_normalization(v_p)
        v_p[2] = 1 if visible else 0

        wall_projection_vertecies.append(Vertex(v_p[0], v_p[1], v_p[2], v_p[3]))

    wall_projection = Wall(wall_projection_vertecies, wall.color)
    return wall_projection

def cube_2_walls(cube):
    walls = []
    walls.append(Wall([cube.vertecies[0], cube.vertecies[1], cube.vertecies[3], cube.vertecies[2]], cube.color))
    walls.append(Wall([cube.vertecies[0], cube.vertecies[1], cube.vertecies[5], cube.vertecies[4]], cube.color))
    walls.append(Wall([cube.vertecies[0], cube.vertecies[2], cube.vertecies[6], cube.vertecies[4]], cube.color))
    walls.append(Wall([cube.vertecies[1], cube.vertecies[3], cube.vertecies[7], cube.vertecies[5]], cube.color))
    walls.append(Wall([cube.vertecies[2], cube.vertecies[3], cube.vertecies[7], cube.vertecies[6]], cube.color))
    walls.append(Wall([cube.vertecies[4], cube.vertecies[5], cube.vertecies[7], cube.vertecies[6]], cube.color))

    return walls

def draw_wall(screen, wall):
    if mode:
        pg.draw.polygon(screen, wall.color, [translate_for_display(wall.vertecies[0]), translate_for_display(wall.vertecies[1]), translate_for_display(wall.vertecies[2]), translate_for_display(wall.vertecies[3])])
        pg.draw.aaline(screen, (255,255,255), translate_for_display(wall.vertecies[0]), translate_for_display(wall.vertecies[1]))
        pg.draw.aaline(screen, (255,255,255), translate_for_display(wall.vertecies[1]), translate_for_display(wall.vertecies[2]))
        pg.draw.aaline(screen, (255,255,255), translate_for_display(wall.vertecies[2]), translate_for_display(wall.vertecies[3]))
        pg.draw.aaline(screen, (255,255,255), translate_for_display(wall.vertecies[3]), translate_for_display(wall.vertecies[0]))
    else:
        pg.draw.aaline(screen, wall.color, translate_for_display(wall.vertecies[0]), translate_for_display(wall.vertecies[1]))
        pg.draw.aaline(screen, wall.color, translate_for_display(wall.vertecies[1]), translate_for_display(wall.vertecies[2]))
        pg.draw.aaline(screen, wall.color, translate_for_display(wall.vertecies[2]), translate_for_display(wall.vertecies[3]))
        pg.draw.aaline(screen, wall.color, translate_for_display(wall.vertecies[3]), translate_for_display(wall.vertecies[0]))

def projection_normalization(vtx):
    return [vtx[0]/vtx[3], vtx[1]/vtx[3], vtx[2]/vtx[3], 1]


def translate_for_display(vertex):
    return (screen_width/2 + vertex.x, screen_height/2 - vertex.y)


def translate(dx, dy, dz):
    for cube in cubes:
        for i, vertex in enumerate(cube.vertecies):
            vert = tuple(np.matmul(translation_matrix(dx, dy, dz), vertex.get_tuple()))
            cube.vertecies[i] = Vertex(vert[0], vert[1], vert[2], vert[3])


def tilt(a):
    for cube in cubes:
        for i, vertex in enumerate(cube.vertecies):
            vert = tuple(np.matmul(rot_mat_x(a), vertex.get_tuple()))
            cube.vertecies[i] = Vertex(vert[0], vert[1], vert[2], vert[3])


def pan(a):
    for cube in cubes:
        for i, vertex in enumerate(cube.vertecies):
            vert = tuple(np.matmul(rot_mat_y(a), vertex.get_tuple()))
            cube.vertecies[i] = Vertex(vert[0], vert[1], vert[2], vert[3])


def roll(a):
    for cube in cubes:
        for i, vertex in enumerate(cube.vertecies):
            vert = tuple(np.matmul(rot_mat_z(a), vertex.get_tuple()))
            cube.vertecies[i] = Vertex(vert[0], vert[1], vert[2], vert[3])
