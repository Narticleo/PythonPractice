import cv2
import numpy as np
# r = [170,179, 57,128,184,255]
r = [170,57,184,197,128,255,195,0,255]
# g = [36, 79, 44,143, 88,184]
g = [36,44,88,79,143,184,0,255,4]
# b = [95,110, 53,124, 99,255]
b = [95,53,99,110,124,255,255,242,0]
drawPoint = []
colors = [r,g,b]
def findPens(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    for color in colors:
        lower = np.array(color[:3])
        upper = np.array(color[3:6])    
        mask = cv2.inRange(hsv, lower, upper)
        penx, peny = findContour(mask)
        cv2.circle(contour, (penx, peny), 7, color[6:9], cv2.FILLED)
        drawPoint.append([penx,peny,color[6:9]])
        draw(drawPoint)

def findContour(img):
    contours, heirachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h = -1, -1, -1, -1
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
    return x+w//2, y

def draw(drawPoint):
    for point in drawPoint:
        cv2.circle(contour, (point[0], point[1]), 7, point[2], cv2.FILLED)

# frame = cv2.imread('colorPens.jpg')
while True:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ord('q') == cv2.waitKey(1):
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    contour = frame.copy()
    findPens(frame)
    # cv2.imshow('frame', frame)
    cv2.imshow('contour', contour)
