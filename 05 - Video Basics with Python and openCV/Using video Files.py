

import cv2
import time
cap = cv2.VideoCapture("mysupervideo.mp4")

if cap.isOpened() == False:
    print('ERROR FILE NOT FOUND or WRONG CODE USED!')

while cap.isOpened():
    ret,frame = cap.read()

    if ret == True:

        # WRITER 20 FPS
        time.sleep(1/20)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    else:
        break