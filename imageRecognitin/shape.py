import cv2

shape = cv2.imread('shape.jpg')
shape = cv2.resize(shape, (0, 0), fx = 2, fy = 2)
canny = cv2.Canny(shape, 150, 200)
contour, heirachy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contour:
    cv2.drawContours(shape, cnt, -1, (100, 100, 0), 3)
    # print(cv2.contourArea(cnt))
    # print(cv2.arcLength(cnt, True))
    perimeter = cv2.arcLength(cnt, True)
    if perimeter > 100:
        vertices = cv2.approxPolyDP(cnt , perimeter*0.05, True)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(shape, (x, y), (x+w, y+h), (0, 100, 100), 3)
        print(len(vertices))
        if len(vertices) == 3:
            cv2.putText(shape, 'triangle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 250, 0), 1)
        elif len(vertices) == 4:
            cv2.putText(shape, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 250, 0), 1)
        elif len(vertices) == 5:
            cv2.putText(shape, 'pentagon', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 250, 0), 1)
        else:
            cv2.putText(shape, 'circle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 250, 0), 1)

cv2.imshow('canny', canny)
cv2.imshow('shape', shape)
cv2.waitKey(0)