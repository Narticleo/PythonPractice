import cv2
import numpy as np

blue = np.array([90, 107, 114, 108, 183, 255, 255, 228, 51])
pink = np.array([129, 98, 138, 178, 231, 255, 229, 102, 255])
green = np.array([46, 43, 0, 64, 255, 255, 10, 255, 18])
colors = [blue, pink, green]
points = []
def findpen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in colors:
        filtered = cv2.inRange(hsv, color[:3], color[3:6])
        canny = cv2.Canny(filtered, 150, 200)
        # cv2.imshow('canny', canny)
        contours ,heirachy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y ,w, h = cv2.boundingRect(contour)
                points.append( (x+w//2, y, color[6:9]) )
                cv2.drawContours(img, contour, -1, color[6:9].tolist(), 3)
    draw(img)
    cv2.imshow('img', img)

def draw(img):
    for point in points:
        cv2.circle(img, (point[0], point[1]), 10, point[2].tolist(), cv2.FILLED) #???


cap = cv2.VideoCapture('allColors.mp4')
while True:
    if cv2.waitKey(31) == ord('q'):
        break
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5)
    findpen(frame)