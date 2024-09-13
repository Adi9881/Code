import cv2 as cv
import os
import numpy as np
cascade = cv.CascadeClassifier("C:\\Users\\adija\\Downloads\\haarcascade_frontalface_default.xml")
reco = cv.face.LBPHFaceRecognizer_create()
reco.read("C:\\Users\\adija\\Desktop\\Code\\training.yaml")
font = cv.FONT_HERSHEY_SIMPLEX
id = 1
names = ['None', 'Adi', 'Adi2']
cam = cv.VideoCapture(0)
cam.set(3, 1080)
cam.set(4, 1960) 
minwid = 0.1*cam.get(3)
minhght = 0.1*cam.get(4)
while True:
    ret, img =cam.read()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minwid), int(minhght)),
       )
    for(x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, conf = reco.predict(gray[y:y+h,x:x+w])
        if (conf < 100):
            id = names[id]
            conf = "{0}%".format(round(100 - conf))
        else:
            id = "unknown"
            conf = "{0}%".format(round(100 - conf))
        cv.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv.putText(img, str(conf), (x+5,y+h-5), font, 1, (255,255,0), 1)
    cv.imshow('camera',img)
    k = cv.waitKey(10) & 0xff 
    if k == 27:
        break
print("\n Execution Successful")
cam.release()
cv.destroyAllWindows()