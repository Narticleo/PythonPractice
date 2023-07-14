import cv2
import numpy as np

color = np.zeros((300,300,3), np.uint8)

for i in range(300):
    for j in range(300):
        color[i][j] = [195, 0, 255]

cv2.imshow('color',color)
cv2.waitKey(0)