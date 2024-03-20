import pygame as pg
import elements as el
from colour import *
from math import floor, ceil
import elements as el


pg.init()


set_object = {}


class Window:
    def __init__(self, cord_o, cord, m = 10, f = True):
        self.cord_o = cord_o
        self.cord = cord
        self.xo, self.yo = cord_o
        self.x, self.y = cord
        self.m = m
        self.f = f
    
    def hole(self, surface, colour, w):
        pg.draw.rect(surface, colour, (self.xo, self.yo, self.x, w.yo - self.yo))
        pg.draw.rect(surface, colour, (self.xo, w.yo, w.xo - self.xo, w.y))
        pg.draw.rect(surface, colour, (w.xo + w.x, w.yo, self.x - w.xo - w.x, w.y))
        pg.draw.rect(surface, colour, (self.xo, w.y + w.yo, self.x, self.y - w.y - w.yo))

w = Window((0, 0), (800, 400), 20)
plan = Window((0, 0), (w.x * 0.8, w.y * 0.8), 20)

_w_ = pg.display.set_mode((w.x, w.y))
pg.display.set_caption('Ы-Ы-Ы-Ы-Ы')



class Mouse:
    def __init__(self, w):
        self.f = [False, False, False,
            False, False, False, False]
        self.w = w
        self.x = 0
        self.y = 0
        self.dx = int(w.x / 2)
        self.dy = int(w.y / 2)
    

    def main(self, e):
        self.__size(e)
        self.__mov(e)

    def __size(self, e):
        if self.f[1]:
            step = 4
        else:
            step = 1

        if self.f[3]:
            self.w.m += step
        elif self.f[4] and self.w.m > 4:
            self.w.m -= 1
    

    def __mov(self, e):
        if e.type == pg.MOUSEBUTTONUP:
            self.f[e.button - 1] = False
        elif True in self.f:
            self.__events(e, self.f.index(True))
        elif e.type == pg.MOUSEBUTTONDOWN:
            self.f[e.button - 1] = True
            if e.button == 1:
                self.__events(e, 0)
            self.x, self.y = pg.mouse.get_pos()
            
    def __events(self, e, key):
        if key == 0:
            x, y = pg.mouse.get_pos()
            x -= self.dx
            x //= self.w.m
            y -= self.dy
            y //= self.w.m
            y *= -1
            set_object[(x, y)] = 1


            return 
        elif key == 2:
            x, y = pg.mouse.get_pos()
            if (self.w.xo <= x <= self.w.x and
            self.w.yo <= y <= self.w.y):
                self.dx += x - self.x
                self.dy += y - self.y
            self.x = x; self.y = y

m = Mouse(plan)


class Coordinate_network:
    def __init__(self, w, network_colour, center_colour = None):
        self.w = w
        self.matrix = [[], [], [], []]
        self.dx = 0; self.dy = 0
        self.network_colour = network_colour
        if center_colour == None:
            self.center_colour = anti(network_colour)
        else:
            self.center_colour = center_colour


    def art(self, _w_, d):
        if (self.dx, self.dx) != d:
            self.dx = d[0]; self.dy = d[1]

            self.__matrix_art(_w_, self.__matrix_fill())

            pg.draw.line(_w_, self.center_colour, (self.w.xo, self.w.yo + d[1]), (self.w.x, self.w.yo + d[1]), 2)
            pg.draw.line(_w_, self.center_colour, (self.w.xo + d[0], self.w.yo), (self.w.xo + d[0], self.w.y), 2)
            
            for i in self.matrix:
                if i:
                    for y in i:
                        print(y)
                else:
                    print(i)
                print()
            print('-' * 20)


    def __matrix_fill(self):
        un = lambda x: 0 if x < 0 else x
        result = []
        def f(x, xo, y, yo):
            x, xo, y, yo = map(lambda x: x / self.w.m, [x, xo, y, yo])
            xo, yo = map(floor, [xo, yo])
            x, y = map(lambda x: x + 1, map(ceil, [x, y]))
            result.append([x, xo, y, yo])
            return x, xo, y, yo

        # I:
        x = self.w.x - self.dx
        xo = un(self.w.xo - self.dx)
        y = self.dy - self.w.yo
        yo = un(self.dy - self.w.y)

        x, xo, y, yo = f(x, xo, y, yo)
        self.matrix[0] = [[set_object.get((j, i), 0) for j in range(xo, x)] for i in range(yo, y)]

        # II:
        x = self.dx - self.w.xo
        xo = un(self.dx - self.w.x)
        y = self.dy - self.w.yo
        yo = un(self.dy - self.w.y)

        x, xo, y, yo = f(x, xo, y, yo)
        self.matrix[1] = [[set_object.get((-j, i), 0) for j in range(xo, x)] for i in range(yo, y)]

        # III:
        x = self.dx - self.w.xo
        xo = un(self.dx - self.w.x)
        y = self.w.y - self.dy
        yo = un(self.w.yo - self.dy)

        x, xo, y, yo = f(x, xo, y, yo)
        self.matrix[2] = [[set_object.get((-j, -i), 0) for j in range(xo, x)] for i in range(yo, y)]

        # IV:
        x = self.w.x - self.dx
        xo = un(self.w.xo - self.dx)
        y = self.w.y - self.dy
        yo = un(self.w.yo - self.dy)

        x, xo, y, yo = f(x, xo, y, yo)
        self.matrix[3] = [[set_object.get((j, -i), 0) for j in range(xo, x)] for i in range(yo, y)]

        return result


    def __matrix_art(self, surface, pos) -> None:
        set_f = (lambda i, j, x, y: [j + x, -i - y],
                 lambda i, j, x, y: [-j - x, -i - y],
                 lambda i, j, x, y: [-j - x, i + y],
                 lambda i, j, x, y: [j + x, i + y])
        for m in range(4):
            xo, x, yo, y = pos[m]
            if self.matrix[m]:
                f = set_f[m]
                for i in range(yo - y):
                    for j in range(xo - x):
                        size = f(i, j, x, y) + [1, 1]
                        size = list(map(lambda x: x * self.w.m, size))
                        size[0] += self.dx
                        size[1] += self.dy
                        if self.matrix[m][i][j]:
                            pg.draw.rect(surface, self.network_colour, size)
                        else:
                            pg.draw.rect(surface, self.network_colour, size, 1)
        print(pos, '\n')        

                
    


cord = Coordinate_network(plan, anti(RED), RED)
x, y = 100, 100



while w.f:
    pg.display.flip()
    _w_.fill(WHITE)

    pg.draw.rect(_w_, BLUE, (plan.xo, plan.yo, plan.x, plan.y), 1)
    cord.art(_w_, (m.dx, m.dy))
    w.hole(_w_, (200, 200, 200), plan)

    for e in pg.event.get():
        if e.type == pg.QUIT:
            w.f = False
        elif e.type == pg.KEYDOWN and e.key == 27:
            w.f = False

        m.main(e)
    print((m.x, m.y), (m.dx, m.dy), m.f)