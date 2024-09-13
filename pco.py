import cv2 as cv
import os
sample = 0
k = 0
cap = cv.VideoCapture(0)
cap.set(3, 1080)
cap.set(4, 1960)
cascade = cv.CascadeClassifier('haarcascffdefault.xml')
id = int(input("Enter the ID of the user : "))
while (True) :
    ret, img = cap.read()
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(grey, 1.1, 3)
    for x, y, w, h in faces :
        path = 'C:\\Users\\adija\\facerecognition\\collection'
        sample = sample + 1
        cv.imwrite("C:\\Users\\adija\\facerecognition\\collection" + str(id) + '.' + str(sample) + ".jpg", grey[y:y+h,x:x+w])
        k = cv.waitKey(100) & 0xff
    if k == 27 :
        break
    elif sample >= 50 :
         break
cap.release()
cv.destroyAllWindows()
print("Execution successful")
