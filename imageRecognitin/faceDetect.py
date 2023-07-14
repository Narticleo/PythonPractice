import cv2

althea = cv2.imread('19&20.jpg')
althea = cv2.resize(althea, (0, 0), fx = 0.5, fy = 0.5)

# althea = cv2.imread('inoueTakina.jpg')
# althea = cv2.resize(althea, (0, 0), fx = 0.5, fy = 0.5)

faceCascade = cv2.CascadeClassifier('faceDetect.xml')
gray = cv2.cvtColor(althea, cv2.COLOR_BGR2GRAY)

faceRect = faceCascade.detectMultiScale(gray, 1.005, 25)
print(len(faceRect))

for (x, y, w, h) in faceRect:
    cv2.rectangle(althea, (x, y), (x+w, y+h), (250,0,250), 1)

cv2.imshow('althea_face', althea)
cv2.waitKey(0)