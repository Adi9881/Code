import cv2 as cv
key = 0
cap = cv.VideoCapture(0)
cap.set(4, 1960)
cap.set(3, 1080)
while (True) :
    ret, frame = cap.read()
    if ret :
     cv.imshow("Video", frame)
    if key == ord("d"):
        break
cap.release()
cv.destroyAllWindows()

# h