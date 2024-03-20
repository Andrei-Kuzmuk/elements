import pygame as pg


class Elements():
    def __init__(self) -> None:
        self.num = __class__.__name__
        self.name
        self.q = 0
    
    def button(self):
        pg.draw.rect(surface, color, coords)
        pg.draw.rect(surface, color, coords, 2)




class Empty(Elements):
    def __init__(self) -> None:
        super().__init__()
        ...
    def art(self):
        ...

class Wire(Elements):
    def __init__(self) -> None:
        super().__init__()
        ...
    def art(self):
        ...

class Key(Elements):
    def __init__(self) -> None:
        super().__init__()
        ...
    def art(self):
        ...

class Bridge(Elements):
    def __init__(self) -> None:
        super().__init__()
        ...
    def art(self):
        ...


class Lamp(Elements):
    def __init__(self) -> None:
        super().__init__()
        ...
    def art(self):
        ...

class NOT(Elements):
    def __init__(self) -> None:
        super().__init__()
        ...
    def art(self):
        ...

class END(Elements):
    def __init__(self) -> None:
        super().__init__()
        ...
    def art(self):
        ...

class OR(Elements):
    def __init__(self) -> None:
        super().__init__()
        ...
    def art(self):
        ...