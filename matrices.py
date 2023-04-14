import numpy as np
from math import cos, sin, radians


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
