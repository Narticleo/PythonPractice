import cv2
import numpy as np

color =[1, 2, [100,100,100]]
img = cv2.imread('althea.jpg')
img = cv2.resize(img, (0,0), fx = 0.15, fy = 0.15)
cv2.circle(img, (270,400), 50, list(color[2]), cv2.FILLED)
cv2.circle(img, (270,400), 20, (0, 0, 0, 255), cv2.FILLED)
cv2.imshow('althea', img)
cv2.waitKey(0)