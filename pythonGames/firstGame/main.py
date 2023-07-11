import pygame as pg
import random as rd
from PIL import Image
import os
HEIGHT = 600
WIDTH = 500
SIZE = (WIDTH,HEIGHT)
BLACK = (0,0,0)
BROWN = (255,77,0)
GOLDEN = (255,215,0)
WHITE = (246,246,246)
BLUE = (30, 144, 255)
FPS = 60

pg.init()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("testing")

#load imgs
img_background = pg.image.load(os.path.join("imgs","background.jpg")).convert()
img_background = pg.transform.scale(img_background,(500,600))
img_ship = pg.image.load(os.path.join("imgs","ship.jpg")).convert()
img_bullet = pg.image.load(os.path.join("imgs","bullet.png")).convert()
img_meteorites = []
for i in range(2):
    img_meteorites.append(pg.image.load(os.path.join("imgs", f"meteorite{i}.png")).convert())
for i in range(2,6):
    img_meteorites.append(pg.image.load(os.path.join("imgs", f"meteorite{i}.jpg")).convert())
img_meteorites.append(pg.image.load(os.path.join("imgs", "meteorite6.webp")).convert())




clock = pg.time.Clock()
all_sprite = pg.sprite.Group()
meteorites = pg.sprite.Group()
bullets = pg.sprite.Group()

#class Battleship
class Battleship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = img_ship
        self.image = pg.transform.scale(self.image, (38,50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT - self.rect.height/2 - 10
        self.radius = 20
        pg.draw.circle(self.image, BLUE, self.rect.center, self.radius)
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
    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.top)
        all_sprite.add(bullet)
        bullets.add(bullet)

#class Meteorite    
class Meteorite(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image_ori = rd.choice(img_meteorites)
        self.p = rd.randrange(6,15)
        self.image_ori = pg.transform.scale(self.image_ori,(5*self.p,4*self.p))
        pix = self.image_ori.get_at([0,0])
        self.image_ori.set_colorkey(pix)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.initializeParameter()
        self.totalDegree = 0
        self.degree = rd.randrange(-5,5)
    def initializeParameter(self):
        self.rect = self.image.get_rect()
        self.rect.x = rd.randrange(0,WIDTH - self.rect.width)
        self.rect.y = rd.randrange(-100,-60)
        self.speedx = rd.randrange(-5,5)
        self.speedy = rd.randrange(4,10)
    def rotate(self):
        self.totalDegree += self.degree
        self.totalDegree %= 360
        self.image = pg.transform.rotate(self.image_ori, self.totalDegree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
    def update(self):
        self.rotate()
        if self.rect.top > HEIGHT:
            self.initializeParameter()
        if self.rect.left <= 0 or self.rect.right > WIDTH:
            self.speedx *= -1
        self.rect.x += self.speedx
        self.rect.y += self.speedy

#class bullet
class Bullet(pg.sprite.Sprite):
    def __init__(self,startx,starty):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((8,15))
        self.image = img_bullet
        self.image = pg.transform.scale(self.image,(40,30))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = startx
        self.rect.bottom = starty + 3
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

ship = Battleship()
all_sprite.add(ship)
for i in range(7):
    meteorite = Meteorite()
    all_sprite.add(meteorite)
    meteorites.add(meteorite)

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LCTRL:
                ship.shoot()

    collides = pg.sprite.groupcollide(bullets, meteorites, True, True)
    while meteorites.__len__() < 8:
        m = Meteorite()
        all_sprite.add(m)
        meteorites.add(m)

    collides = pg.sprite.spritecollide(ship, meteorites, True, pg.sprite.collide_circle)
    # if collides:
    #     running = False
    
    all_sprite.update()
    screen.blit(img_background,(0,0))
    all_sprite.draw(screen)
    pg.display.update()

pg.quit()