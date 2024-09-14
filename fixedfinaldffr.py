import cv2 as cv
from deepface import DeepFace
import time

ESC_KEY = 27
FRAME_INTERVAL = 100

reference_imgs = {
    'jay': cv.imread("C:\\Users\\adija\\OneDrive\\Pictures\\Camera Roll\\WIN_20240913_20_19_22_Pro.jpg"),
    'adi': cv.imread("C:\\Users\\adija\\OneDrive\\Pictures\\Camera Roll\\WIN_20240913_13_29_22_Pro.jpg"),
    'aman': cv.imread("C:\\Users\\adija\\OneDrive\\Pictures\\Camera Roll\\WIN_20240913_13_29_22_Pro.jpg"),
    'dhruv': cv.imread("C:\\Users\\adija\\OneDrive\\Pictures\\Camera Roll\\WIN_20240913_13_29_22_Pro.jpg"),
    'renesh': cv.imread("C:\\Users\\adija\\OneDrive\\Pictures\\Camera Roll\\WIN_20240913_13_29_22_Pro.jpg")
}

def verify_face(frame, reference_img):
    try:
        start_time = time.time()
        result = DeepFace.verify(frame, reference_img.copy())['verified']
        print(f"Verification time: {time.time() - start_time:.2f} seconds")
        return result
    except ValueError as e:
        print(f"Error verifying face: {e}")
        print(f"Reference image shape: {reference_img.shape}")
        print(f"Reference image dtype: {reference_img.dtype}")
        return False

cap = cv.VideoCapture(0)
cap.set(4, 640)  
cap.set(3, 480)

counter = 0
face_matches = {}

while True:
    ret, frame = cap.read()
    if ret:
        if counter % FRAME_INTERVAL == 0:
            for name, reference_img in reference_imgs.items():
                face_matches[name] = verify_face(frame.copy(), reference_img)
        counter += 1
        for name, match in face_matches.items():
            if match:
                cv.putText(frame, f"{name.upper()}!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                break
        else:
            cv.putText(frame, "NO MATCH!", (20, 450), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv.imshow("Video", frame)
        key = cv.waitKey(30)
        if key == ESC_KEY:
            break

cv.destroyAllWindows()