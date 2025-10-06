from os import system
from math import sqrt, floor

class World2D:
    def __init__(self):
        self.tiles = [[' ' for j in range(20)] for i in range(20)]
        self.draw()

    def set_tile(self, char, x, y):
        self.tiles[y][x] = char

    def draw_line(self, char, x0, y0, x, y):
        start = Vector2D(x0, y0)
        end = Vector2D(x, y)
        diff = (start - end)
        diff_normalized = diff.normalize()
        diff_abs = diff.abs()

        point = start
        for i in range(floor(diff_abs)):
            point = point + diff_normalized


    def draw_rect(self, char, x0, y0, x, y):
        pass

    def update(self):
        for y in range(len(self.tiles)):
            print(''.join([self.tiles[y][x] for x in range(len(self.tiles[y]))]))
        system('cls')

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def abs(self):
        return sqrt(self.x**2 + self.y**2)

    def normalize(self):
        return Vector2D(self.x/self.abs(), self.y/self.abs())

    def __sub__(self, other):
        return Vector2D(self.x-other.x,self.y-other.y)

    def __add__(self, other):
        return Vector2D(self.x+other.x,self.y+other.y)

world = World2D()
world.set_tile('s', 5, 5)
world.update()
input()
