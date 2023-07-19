import cv2
import numpy as np
def empty(v):
    pass

cv2.namedWindow('trackbar')
cv2.createTrackbar('min hue', 'trackbar', 0, 179, empty)
cv2.createTrackbar('max hue', 'trackbar', 179, 179, empty)
cv2.createTrackbar('min sat', 'trackbar', 0, 255, empty)
cv2.createTrackbar('max sat', 'trackbar', 255, 255, empty)
cv2.createTrackbar('min bri', 'trackbar', 0, 255, empty)
cv2.createTrackbar('max bri', 'trackbar', 255, 255, empty)

cap = cv2.VideoCapture('green.mp4')
cap.read()
ret, frame = cap.read()
frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
cv2.circle(frame, (325, 175), 20, (255, 255, 255), -1)
f1 = frame.copy()
h1 = cv2.cvtColor(f1, cv2.COLOR_BGR2HSV)
m1 = cv2.inRange(h1, (0, 0, 255), (0, 0, 255))
hsv =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
cv2.circle(f1, (325, 175), 40, (255, 0, 0), -1)


while True:
    if cv2.waitKey(31) == ord('q'):
        break
    cv2.imshow('m1', m1)
    minh = cv2.getTrackbarPos('min hue', 'trackbar')
    maxh = cv2.getTrackbarPos('max hue', 'trackbar')
    mins = cv2.getTrackbarPos('min sat', 'trackbar')
    maxs = cv2.getTrackbarPos('max sat', 'trackbar')
    minb = cv2.getTrackbarPos('min bri', 'trackbar')
    maxb = cv2.getTrackbarPos('max bri', 'trackbar')
    lower = np.array([minh, mins, minb])
    upper = np.array([maxh, maxs, maxb])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.imshow('f1', f1)
    r1 = cv2.bitwise_xor(f1, frame, mask = m1)
    cv2.imshow('r1', r1)