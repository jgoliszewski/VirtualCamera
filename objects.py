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