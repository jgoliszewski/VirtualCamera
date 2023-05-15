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

class Wall:
    def __init__(self, vertecies, color):
        self.vertecies = vertecies
        self.color = color
    
    def get_CofG(self):
        return (self.vertecies[0].z + self.vertecies[1].z + self.vertecies[2].z + self.vertecies[3].z) / 4
    
    
    def get_normal(self):
        v1 = np.array([self.vertecies[0].x, self.vertecies[0].y, self.vertecies[0].z])
        v2 = np.array([self.vertecies[1].x, self.vertecies[1].y, self.vertecies[1].z])
        v3 = np.array([self.vertecies[2].x, self.vertecies[2].y, self.vertecies[2].z])
        return np.cross(v2 - v1, v3 - v1)
    
    def __ge__(self, other):
        normal = other.get_normal()
        v = other.vertecies[0]
        for vertex in self.vertecies:
            if vertex.x == v.x and vertex.y == v.y and vertex.z == v.z:
                continue

            vector = np.array([vertex.x-v.x, vertex.y-v.y, vertex.z-v.z])

            a = np.dot(vector, normal)
            if a > 0:
                return False
            elif a < 0:
                return True
            else:
                continue

    # def __ge__(self, other):
    #     return self.get_CofG() >= other.get_CofG()
  
        
