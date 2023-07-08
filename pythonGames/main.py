import pygame as pg
import random as rd
HEIGHT = 600
WIDTH = 500
SIZE = (WIDTH,HEIGHT)
BLACK = (0,0,0)
BROWN = (255,77,0)
GOLDEN = (255,215,0)
BACKGROUND = (30, 144, 255)
FPS = 60

pg.init()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("testing")
clock = pg.time.Clock()
#class Player
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT - self.rect.height/2 - 10
        self.speedx = 10
        self.speedy = 10
    def update(self):
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speedx
        if key_pressed[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speedx
        if key_pressed[pg.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speedy
        if key_pressed[pg.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speedy
#class bullet
class Bullet(pg.sprite.Sprite):
    def __init__(self,player,starty):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((8,15))
        self.image.fill(GOLDEN)
        self.rect = self.image.get_rect()
        self.player = player
        self.speedy = 5
        self.starty = starty
        self.setStartPoint()
    def setStartPoint(self):
        self.rect.centerx = self.player.rect.centerx
        self.rect.bottom =  self.player.rect.top - self.starty 
    def update(self):
        if self.rect.bottom < 0: 
            self.setStartPoint()
        self.rect.y -= self.speedy
#class Meteorite    
class Meteorite(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,40))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.initializeParameter()
    def initializeParameter(self):
        self.rect = self.image.get_rect()
        self.rect.x = rd.randrange(0,WIDTH - self.rect.width)
        self.rect.y = rd.randrange(-100,-60)
        self.speedx = rd.randrange(-5,5)
        self.speedy = rd.randrange(4,10)

    def update(self):
        if self.rect.top > HEIGHT:
            self.initializeParameter()
        if self.rect.left <= 0 or self.rect.right > WIDTH:
            self.speedx *= -1
        self.rect.x += self.speedx
        self.rect.y += self.speedy


all_sprite = pg.sprite.Group()
player1 = Player()
all_sprite.add(player1)
for i in range(7):
    meteorite = Meteorite()
    all_sprite.add(meteorite)
    bullet = Bullet(player1,i*2)
    all_sprite.add(bullet)

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