import cv2
import numpy as np
def empty(v):
    pass
img = cv2.imread('althea2.jpg')
img = cv2.resize(img, (0, 0), fx = 0.15, fy = 0.15)
# img = img[:img.shape[0]][:int(0.9*img.shape[1])]       ??????????????
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('trackbar')
cv2.resizeWindow('trackbar', 640, 320)
cv2.createTrackbar('min hue', 'trackbar', 0, 179, empty)
cv2.createTrackbar('max hue', 'trackbar', 179, 179, empty)
cv2.createTrackbar('min sat', 'trackbar', 0, 255, empty)
cv2.createTrackbar('max sat', 'trackbar', 255, 255, empty)
cv2.createTrackbar('min bri', 'trackbar', 0, 255, empty)
cv2.createTrackbar('max bri', 'trackbar', 255, 255, empty)

while True:
    h_min = cv2.getTrackbarPos('min hue', 'trackbar')
    h_max = cv2.getTrackbarPos('max hue', 'trackbar')
    s_min = cv2.getTrackbarPos('min sat', 'trackbar')
    s_max = cv2.getTrackbarPos('max sat', 'trackbar')
    b_min = cv2.getTrackbarPos('min bri', 'trackbar')
    b_max = cv2.getTrackbarPos('max bri', 'trackbar')
    lower, upper = (h_min, s_min, b_min), (h_max, s_max, b_max)
    mask = cv2.inRange(hsv , lower, upper)
    result = cv2.bitwise_and(img, img , mask = mask)
    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.waitKey(1)