WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


mix = lambda a, b: tuple([(a[i] + b[i]) // 2 for i in range(3)])
anti = lambda i: tuple(map(lambda j: 255 - j, i))