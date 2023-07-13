import cv2
althea = cv2.imread("althea.jpg")
inoue = cv2.imread("inoueTakina.jpg")
althea = cv2.resize(althea, (0,0), fx = 0.15, fy = 0.15)
inoue = cv2.resize(inoue, (0,0), fx = 0.5, fy = 0.5)

img = althea[:althea.shape[0]][:althea.shape[1]]
cv2.imshow("althea",img)
cv2.waitKey(0)
