import cv2 as cv
key = 0
cap = cv.VideoCapture(0)
cap.set(4, 1960)
cap.set(3, 1080)
while key != 27:
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    key = cv.waitKey(1)
cap.release()
cv.destroyAllWindows()

# h