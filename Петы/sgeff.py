from os import system
from math import sqrt, floor

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def abs(self):
        return sqrt(self.x**2 + self.y**2)

    def normalized(self):
        return Vector2D(self.x/self.abs(), self.y/self.abs())

    def __floor__(self):
        return Vector2D(floor(self.x), floor(self.y))

    def __round__(self, n=None):
        return Vector2D(round(self.x), round(self.y))

    def __sub__(self, other):
        return Vector2D(self.x-other.x,self.y-other.y)

    def __add__(self, other):
        return Vector2D(self.x+other.x,self.y+other.y)

    def __mul__(self, other):
        return Vector2D(self.x*other, self.y*other)

    def __truediv__(self, other):
        return Vector2D(self.x/other, self.y/other)

    def __str__(self):
        return f'Vector2D({self.x}, {self.y})'

class World2D:
    def __init__(self, size: Vector2D):
        self.size = size
        self.tiles = [[' ' for j in range(self.size.x)] for i in range(self.size.y)]
        self.update()

    def set_tile(self, char: str, tile: Vector2D):
        self.tiles[tile.y][tile.x] = char

    def draw_line(self, char: str, start: Vector2D, end: Vector2D):
        diff = end - start
        #diff = Vector2D(abs(diff.x), abs(diff.y))
        diff_normalized = diff.normalized()
        diff_abs = diff.abs()
        steps = int(diff_abs / diff_normalized.abs())+1

        for step in range(0, steps):
            tile = start + round(diff_normalized * step)
            print(tile)
            self.set_tile(char, tile)

    def draw_rect(self, char: str, start: Vector2D, size: Vector2D):
        self.draw_line(char, start, start+Vector2D(size.x, 0))
        self.draw_line(char, start+Vector2D(size.x, 0), start+size)
        self.draw_line(char, start, start+Vector2D(0, size.y))
        self.draw_line(char, start+Vector2D(0, size.y), start+size)

    def update(self):
        system('cls')
        self.__draw_interface__()
        for y in range(len(self.tiles)):
            print(''.join([self.tiles[y][x] for x in range(len(self.tiles[y]))]))

    def __draw_interface__(self):
        print('SGEFF Prototype v. Simple Graphical Engine for Fun')

world = World2D(Vector2D(80, 28))
#world.set_tile('s', Vector2D(0, 0))
#world.draw_line('l', Vector2D(1, 1), Vector2D(20, 5))

world.draw_rect('0', Vector2D(10, 10), Vector2D(8, 7))
world.draw_rect('#', Vector2D(5, 5), Vector2D(10, 10))
world.update()
input()
