import pygame as pg, sys
from pygame.locals import *

W = 500
s = pg.display.set_mode((W, W))
pg.display.set_caption("Surface")
clock = pg.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (100, 255, 100)

class Plane:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def draw(self): pg.draw.polygon(s, WHITE, (self.p1, self.p2, self.p3, self.p4))

p1 = [100, 100]
p2 = [100, 400]
p3 = [400, 400]
p4 = [400, 100]

while True:
    s.fill(BLACK)

    square = Plane(p1, p2, p3, p4)
    square.draw()

    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()
    if keys[K_UP]:
        # print('up')
        p1[0] += 1
        p3[0] += 1
        p2[1] -= 5
        p3[1] -= 5
    if keys[K_DOWN]:
        # print('down')
        p1[0] -= 1
        p3[0] -= 1
        p1[1] += 5
        p4[1] += 5
    if keys[K_LEFT]:
        # print('left')
        p2[1] -= 1
        p4[1] -= 1
        p3[0] -= 5
        p4[0] -= 5
    if keys[K_RIGHT]:
        # print('right')
        p2[1] += 1
        p4[1] += 1
        p1[0] += 5
        p2[0] += 5

    if keys[K_BACKSPACE]:
        p1 = [100, 100]
        p2 = [100, 400]
        p3 = [400, 400]
        p4 = [400, 100]

    if keys[K_SPACE]: print(p1, p2, p3, p4)

    clock.tick(60)
    pg.display.update()