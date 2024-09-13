from deepface import DeepFace
import threading
import cv2 as cv
# /.venv/Scripts/activate
# import os
# from PIL import Image
cap = cv.VideoCapture(0)
cap.set(4, 1960)
cap.set(3, 1080)
counter = 0
key = 0
face_match = False
reference_img = cv.imread("C:\\Users\\adija\\OneDrive\\Pictures\\Camera Roll\\WIN_20240913_20_19_22_Pro.jpg")# path = 'absolute path for folder with images goes here'
# use os..join to connect folder and image paths and return list of image paths (ex. ImagePaths = [])
# for imagepath in ImagePaths :
# pillow1 = Image.open(imagepath)
def check_face(frame):
   global face_match
   try :
      if DeepFace.verify(frame, reference_img.copy())['verified'] :
         face_match = True
      # elif conditions with same arguments and return value save reference_img.copy(), which should be replaced by pillow(INDEXNO.).copy()
      else :
         face_match = False
   except ValueError :
      face_match = False
while key != 27 :
    ret, frame = cap.read()
    if ret : 
     if counter % 30 == 0 :
       try :
          threading.Thread(target=check_face, args=(frame.copy(), )).start()
       except ValueError :
          pass
    counter +=1
    if face_match :
       cv.putText(frame, "MATCH!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) # for displaying a specific name, append "MATCH" with said name
    else :
       cv.putText(frame, "NO MATCH!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    cv.imshow("Video", frame)
    cv.waitKey(1)
cv.destroyAllWindows()


