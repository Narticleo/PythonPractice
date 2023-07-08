import pygame as pg
HEIGHT = 600
WIDTH = 500
SIZE = (WIDTH,HEIGHT)
BLACK = (0,0,0)
BACKGROUND = (30, 144, 255)
FPS = 60

pg.init()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("testing")
clock = pg.time.Clock()

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
    def update(self):
        if self.rect.left == WIDTH-1 or self.rect.left == WIDTH:
            self.rect.right = 0
        else:
            self.rect.x+=2
        if HEIGHT/2 - self.rect.top > self.rect.height/2:
            self.rect.y+=10
        elif HEIGHT/2 - self.rect.top < self.rect.height/2:
            self.rect.y-=10
        else:
            self.rect.y+=5

all_sprite = pg.sprite.Group()
player1 = Player()
all_sprite.add(player1)

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(BACKGROUND)
    all_sprite.update()
    all_sprite.draw(screen)
    pg.display.flip()

pg.quit()