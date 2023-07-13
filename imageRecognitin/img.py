import cv2
import numpy as np
import random as rd

img = np.empty((300, 300, 3), np.uint8)

for i in range(0,300):
    for j in range(0,300):
        img[i][j] = [rd.randint(0,100), rd.randint(0,100), rd.randint(0,100)]

cv2.imshow('img', img)
cv2.waitKey(0)
    