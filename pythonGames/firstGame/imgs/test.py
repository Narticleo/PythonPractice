import pygame as pg
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

imgs = []
for i in range (3,5):
    imgs.append(pg.image.load(os.path.join(f"meteorite{i}.jpg")).convert())

ship = pg.image.load("ship.jpg").convert()
pix = ship.get_at([0,0])[0:3]
print(pix)

print(pg.Surface.get_at([0,0]))




# import pygame as pg

# # 初始化 Pygame
# pg.init()

# # 載入圖片
# image = pg.image.load("bullet.png")

# # 取得圖片的寬度和高度
# width = image.get_width()
# height = image.get_height()

# # 遍歷每個像素
# for y in range(height):
#     for x in range(width):
#         # 獲取指定位置的顏色值
#         color = image.get_at((x, y))

#         # 獲取 RGB 資訊
#         r, g, b = color[0], color[1], color[2]

#         # 顯示 RGB 資訊
#         print(f"Pixel at ({x}, {y}) - R: {r}, G: {g}, B: {b}")

# # 關閉 Pygame
# pg.quit()
