from PIL import Image

im = Image.open('ships.jpg')
pix = im.load()
# width = im.size[0]
# height = im.size[1]
# for x in range(width):
#     for y in range(height):
#         r, g, b = pix[x, y]
print(pix[0,0])

