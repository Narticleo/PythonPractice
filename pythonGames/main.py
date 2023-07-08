import pygame as pg
HEIGHT = 600
WIDTH = 500
SIZE = (WIDTH,HEIGHT)
BACKGROUND = (30, 144, 255)
FPS = 60

pg.init()
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()
running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(BACKGROUND)
    pg.display.update()

pg.quit()