import cv2
import numpy as np

althea = cv2.imread('althea.jpg')
althea = cv2.resize(althea, (0, 0), fx = 0.2, fy = 0.2)

althea_gray = cv2.cvtColor(althea, cv2.COLOR_BGR2GRAY)
althea_blur = cv2.GaussianBlur(althea, (7,7), 10)
althea_canny = cv2.Canny(althea, 100, 120)
althea_dilate = cv2.dilate(althea_canny, (15, 15,), iterations = 3)
althea_erode = cv2.erode(althea_dilate, (15, 15), iterations = 3)


# cv2.imshow('althea', althea)
# cv2.imshow('althea_gray', althea_gray)
# cv2.imshow('althea_blur', althea_blur)
cv2.imshow('althea_canny', althea_canny)
cv2.imshow('althea_dilate', althea_dilate)
cv2.imshow('althea_erode', althea_erode)
while True:
    if cv2.waitKey(0) == ord('q'):
        break