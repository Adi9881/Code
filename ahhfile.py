from deepface import DeepFace
import threading
import cv2 as cv
# /.venv/Scripts/activate
cap = cv.VideoCapture(0)
cap.set(4, 1960)
cap.set(3, 1080)
counter = 0
key = 0
face_matchadi = False
face_matchjay = False
face_matchaman = False
face_matchdhruv = False
face_matchrenesh = False
reference_img = cv.imread("C:\\Users\\adija\\OneDrive\\Pictures\\Camera Roll\\WIN_20240913_20_19_22_Pro.jpg")
def check_faceAdi(frame):
   global face_matchadi
   try :
      if DeepFace.verify(frame, reference_img.copy())['verified'] :
         face_matchadi = True
      else :
         face_matchadi = False
   except ValueError :
      face_matchadi = False
while key != 27 :
    ret, frame = cap.read()
    if ret : 
     if counter % 30 == 0 :
       try :
          threading.Thread(target=check_faceAdi, args=(frame.copy(), )).start()
       except ValueError :
          pass
    counter +=1
    if face_matchadi :
       cv.putText(frame, "ADI!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) # for displaying a specific name, append "MATCH" with said name
       cv.imshow("Video", frame)
    else :
       pass
def check_faceRenesh(frame):
   global face_matchrenesh
   try :
      if DeepFace.verify(frame, reference_img.copy())['verified'] :
         face_matchrenesh = True
      else :
         face_matchrenesh = False
   except ValueError :
      face_matchrenesh = False
while key != 27 :
    ret, frame = cap.read()
    if ret : 
     if counter % 30 == 0 :
       try :
          threading.Thread(target=check_faceRenesh, args=(frame.copy(), )).start()
       except ValueError :
          pass
    counter +=1
    if face_matchadi :
       cv.putText(frame, "RENESH!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) # for displaying a specific name, append "MATCH" with said name
       cv.imshow("Video", frame)
    else :
       pass      
def check_faceJay(frame):
   global face_matchjay
   try :
      if DeepFace.verify(frame, reference_img.copy())['verified'] :
         face_matchjay = True
      else :
         face_matchjay = False
   except ValueError :
      face_matchjay = False
while key != 27 :
    ret, frame = cap.read()
    if ret : 
     if counter % 30 == 0 :
       try :
          threading.Thread(target=check_faceJay, args=(frame.copy(), )).start()
       except ValueError :
          pass
    counter +=1
    if face_matchadi :
       cv.putText(frame, "JAY!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) # for displaying a specific name, append "MATCH" with said name
    else :
       pass      
def check_faceAman(frame):
   global face_matchaman
   try :
      if DeepFace.verify(frame, reference_img.copy())['verified'] :
         face_matchaman = True
      else :
         face_matchaman = False
   except ValueError :
      face_matchaman = False
while key != 27 :
    ret, frame = cap.read()
    if ret : 
     if counter % 30 == 0 :
       try :
          threading.Thread(target=check_faceAman, args=(frame.copy(), )).start()
       except ValueError :
          pass
    counter +=1
    if face_matchadi :
       cv.putText(frame, "AMAN!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) # for displaying a specific name, append "MATCH" with said name
    else :
       pass      
def check_faceDhruv(frame):
   global face_matchdhruv
   try :
      if DeepFace.verify(frame, reference_img.copy())['verified'] :
         face_matchdhruv = True
      else :
         face_matchdhruv = False
   except ValueError :
      face_matchdhruv = False
while key != 27 :
    ret, frame = cap.read()
    if ret : 
     if counter % 30 == 0 :
       try :
          threading.Thread(target=check_faceDhruv, args=(frame.copy(), )).start()
       except ValueError :
          pass
    counter +=1
    if face_matchadi :
       cv.putText(frame, "DHRUV!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) # for displaying a specific name, append "MATCH" with said name
    else :
       pass
while key != 27 :
    ret, frame = cap.read()
    if ret : 
     if counter % 30 == 0 :
       try :
          threading.Thread(target=check_faceAman, args=(frame.copy(), )).start()
       except ValueError :
          pass
    counter +=1
    if face_matchadi :
       cv.putText(frame, "AMAN!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) # for displaying a specific name, append "MATCH" with said name
    else :
  