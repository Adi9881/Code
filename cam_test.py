import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3, 1080) # set Width
cap.set(4, 1960) # set Height
while(True):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)

        k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()


# extra line to test
