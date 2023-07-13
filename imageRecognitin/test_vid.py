import cv2 

cap = cv2.VideoCapture('althea_vid.mp4')


done = False
while not done:
    done, pic = cap.read()
    if done:
        done = False
    pic = cv2.flip(pic, 1) # 1:horizon, 0:vertical, -1:both
    cv2.imshow('video', pic)
    if cv2.waitKey(31) == ord('q'):
        break 
