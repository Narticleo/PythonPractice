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

        # if self.rect.left >= WIDTH:
        #     self.rect.right = 0
        # else:
        #     self.rect.x+=2
        # if HEIGHT/2 - self.rect.top > self.rect.height/2:
        #     self.rect.y+=10
        # elif HEIGHT/2 - self.rect.top < self.rect.height/2:
        #     self.rect.y-=10
        # else:
        #     self.rect.y+=5

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