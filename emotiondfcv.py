import cv2 as cv
from deepface import DeepFace

face_model = cv.CascadeClassifier("C:\\Users\\adija\\Desktop\\Code\\haarcascffdefault.xml")
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        face = face_model.detectMultiScale(cv.cvtColor(frame, cv.COLOR_BGR2GRAY), 1.3, 5)
        for x, y, width, height in face:
            emotions = DeepFace.analyze(frame, actions=["emotion"])  
            dominant_emotion = max(emotions, key=lambda x: x["emotion"])["dominant_emotion"]  #lambda kyuki max value return karne dict ka
            cv.putText(frame, dominant_emotion, (x, y+height), cv.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 0), 2)
            cv.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2)
        cv.imshow("Video", frame)
        if cv.waitKey(1) == 27:
            break

cap.release()
cv.destroyAllWindows()