import cv2
import numpy as np

img = np.zeros((600, 400, 3), np.uint8)
cv2.line(img, (0, 0), (400, 600), (200, 0, 0), 3)
cv2.circle(img, (200, 300), 30, (200, 0, 200), cv2.FILLED)
cv2.rectangle(img, (50, 450), (150, 500), (0, 240, 240), 5)
cv2.putText(img, 'althea', (250, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)