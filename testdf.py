from deepface import DeepFace
import threading
import cv2 as cv
cap = cv.VideoCapture(0)
cap.set(4, 1960)
cap.set(3, 1080)
counter = 0
key = 0
face_matchadi = False
face_matchahh = False
face_matchhaman = False
face_matchdhruv = False
face_matchnepal = False
reference_img = cv.imread("C:\\Users\\adija\\Pictures\\Camera Roll\\WIN_20240913_13_29_22_Pro.jpg")
def check_face_Adi(frame):
   global face_matchadi
   try :
      if DeepFace.verify(frame, reference_img.copy())['verified'] :
         face_matchadi = True
      else :
         face_matchadi = False
   except ValueError :
      face_matchadi = False
def check_face_Jay(frame):
   global face_matchahh
   try :
      if DeepFace.verify(frame, reference_img.copy())['verified'] :
         face_matchahh = True
      else :
         face_matchahh = False
   except ValueError :
      face_matchahh = False
def check_face_Aman(frame):
   global face_matchhaman
   try :
      if DeepFace.verify(frame, reference_img.copy())['verified'] :
         face_matchhaman = True
      else :
         face_matchhaman = False
   except ValueError :
      face_matchhaman = False
def check_face_Dhruv(frame):
   global face_matchdhruv
   try :
      if DeepFace.verify(frame, reference_img.copy())['verified'] :
         face_matchdhruv = True
      else :
         face_matchdhruv = False
   except ValueError :
      face_matchdhruv = False
def check_face_Renesh(frame):
   global face_matchnepal
   try :
      if DeepFace.verify(frame, reference_img.copy())['verified'] :
         face_matchnepal = True
      else :
         face_matchnepal = False
   except ValueError :
      face_matchnepal = False
while True :
    ret, frame = cap.read()
    if ret : 
     if counter % 30 == 0 :
       try :
          threading.Thread(target=check_face_Adi, args=(frame.copy(), )).start()
       except ValueError :
          pass
    counter +=1
    if face_matchadi :
       cv.putText(frame, "ADI!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) 
    elif face_matchahh :
       cv.putText(frame, "JAY!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) 
    elif face_matchhaman :
       cv.putText(frame, "AMAN!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) 
    elif face_matchdhruv :
       cv.putText(frame, "DHRUV!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) 
    elif face_matchnepal :
       cv.putText(frame, "RENESH!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3) 
    else :
       cv.putText(frame, "NO MATCH!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    cv.imshow("Video", frame)
    if key == ord("d"):
        break
cv.destroyAllWindows()



