import numpy as np

class Vertex:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    def get_tuple(self):
        return (self.x, self.y, self.z, self.w)

class Cube:
    def __init__(self, vertecies, color):
        self.vertecies = vertecies
        self.color = color

    def get_center_of_cube(self):
        px = (self.vertecies[0].x + self.vertecies[1].x + self.vertecies[2].x + self.vertecies[3].x + self.vertecies[4].x + self.vertecies[5].x + self.vertecies[6].x + self.vertecies[7].x) / 8
        py = (self.vertecies[0].y + self.vertecies[1].y + self.vertecies[2].y + self.vertecies[3].y + self.vertecies[4].y + self.vertecies[5].y + self.vertecies[6].y + self.vertecies[7].y) / 8
        pz = (self.vertecies[0].z + self.vertecies[1].z + self.vertecies[2].z + self.vertecies[3].z + self.vertecies[4].z + self.vertecies[5].z + self.vertecies[6].z + self.vertecies[7].z) / 8
        return Vertex(px, py, pz, 1)

    def get_CofG(self):
        return (self.vertecies[0].z + self.vertecies[1].z + self.vertecies[2].z + self.vertecies[3].z + self.vertecies[4].z + self.vertecies[5].z + self.vertecies[6].z + self.vertecies[7].z) / 8
    
    def __ge__(self, other):
        return self.get_CofG() >= other.get_CofG()
        

class Wall:
    def __init__(self, vertecies, color):
        self.vertecies = vertecies
        self.color = color
    
    def get_CofG(self):
        return (self.vertecies[0].z + self.vertecies[1].z + self.vertecies[2].z + self.vertecies[3].z) / 4
    
    def get_center_of_wall(self):
        px = (self.vertecies[0].x + self.vertecies[1].x + self.vertecies[2].x + self.vertecies[3].x) / 4
        py = (self.vertecies[0].y + self.vertecies[1].y + self.vertecies[2].y + self.vertecies[3].y) / 4
        pz = (self.vertecies[0].z + self.vertecies[1].z + self.vertecies[2].z + self.vertecies[3].z) / 4
        return Vertex(px, py, pz, 1)
    
    def get_normal(self):
        v1 = np.array([self.vertecies[0].x, self.vertecies[0].y, self.vertecies[0].z])
        v2 = np.array([self.vertecies[1].x, self.vertecies[1].y, self.vertecies[1].z])
        v3 = np.array([self.vertecies[2].x, self.vertecies[2].y, self.vertecies[2].z])
        return np.cross(v2 - v1, v3 - v1)
    
    def get_plane(self):
        v1 = self.vertecies[0]
        v2 = self.vertecies[1]
        v3 = self.vertecies[2]
        
        ux = v2.x - v1.x
        uy = v2.y - v1.y
        uz = v2.z - v1.z
        vx = v3.x - v1.x
        vy = v3.y - v1.y
        vz = v3.z - v1.z

        a = uy * vz - uz * vy
        b = uz * vx - ux * vz
        c = ux * vy - uy * vx
        d = (- a * v1.x - b * v1.y - c * v1.z)

        return (a, b, c, d)

    def __ge__(self, other):
        result = checkPointSideAgainstPlane(self.get_plane(), other.get_center_of_wall(), Vertex(0, 0, 0, 1))
        if result > 0:
            return True
        else:
            return False
        
    # def __ge__(self, other):
        # return self.get_CofG() >= other.get_CofG()
    
def pointMatrixMultiplication(matrix, point):
        return matrix[0] * point.x + matrix[1] * point.y + matrix[2] * point.z + matrix[3]

def checkPointSideAgainstPlane(plane, point, zero):
    return pointMatrixMultiplication(plane, point) * pointMatrixMultiplication(plane, zero)