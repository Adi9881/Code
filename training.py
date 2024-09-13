import cv2 as cv
import numpy as np
from PIL import Image
import os
path = 'C:\\Users\\adija\\facerecognition\\collection'
recog = cv.face.LBPHFaceRecognizer_create()
dtct = cv.CascadeClassifier("C:\\Users\\adija\\Desktop\\Code\\haarcascffdefault.xml")
def getImgsLbls(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    samples =[]
    IDs = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') 
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = dtct.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            samples.append(img_numpy[y:y+h,x:x+w])
            IDs.append(id)
    return samples,IDs
print ("\nTraining faces; this may take a few seconds...")
faces,ids = getImgsLbls(path)
recog.train(faces, np.array(ids))
recog.write('C:\\Users\\adija\\Desktop\\Code\\training.yaml')
print("Training successful")