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
all_sprite = pg.sprite.Group()
meteorites = pg.sprite.Group()
bullets = pg.sprite.Group()

#class Battleship
class Battleship(pg.sprite.Sprite):
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
    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.top)
        all_sprite.add(bullet)
        bullets.add(bullet)

#class bullet
class Bullet(pg.sprite.Sprite):
    def __init__(self,startx,starty):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((8,15))
        self.image.fill(GOLDEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = startx
        self.rect.bottom = starty + 3
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

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
            if event.key == pg.K_LSHIFT:
                ship.shoot()

    collides = pg.sprite.groupcollide(bullets, meteorites, True, True)
    for i in range(0,len(collides)):
        m = Meteorite()
        all_sprite.add(m)
        meteorites.add(m)

    collides = pg.sprite.spritecollide(ship, meteorites, True)
    if collides:
        running = False
    
    all_sprite.update()
    screen.fill(BACKGROUND)
    all_sprite.draw(screen)
    pg.display.update()

pg.quit()