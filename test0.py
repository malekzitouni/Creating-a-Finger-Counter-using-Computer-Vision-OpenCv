import time
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)
folder_path = r"C:\Users\T.M.S\OneDrive\Bureau\fingerrs"
file_list = os.listdir(folder_path)
print(file_list)

new_list = []
ptime = 0
detector = HandDetector(detectionCon=0.7)
for file_name in file_list:
    image_path = os.path.join(folder_path, file_name)

    # Check if the image loading is successful
    image = cv2.imread(image_path)
    if image is not None:
        new_list.append(image)
    else:
        print(f"Warning: Failed to load image '{file_name}'.")

cv2.imshow("test", new_list[1])

while True:
    succ, frame = cap.read()
    # Use the HandDetector to find hands in the frame
    hands, frame = detector.findHands(frame)
    if hands and len(hands) >= 2:
        lmlist = hands[0]
        fingers = hands[1]
        fingerup = detector.fingersUp(lmlist)
        fingers_up = detector.fingersUp(fingers)

        if fingerup == [0, 0, 0, 0, 0] and fingers_up==[0,0,0,0,0]:
            img = new_list[0]
        if fingerup == [0, 1, 0, 0, 0] and fingers_up==[0,0,0,0,0]:
            img = new_list[1]
        if fingerup == [0, 1, 1, 0, 0] and fingers_up==[0,0,0,0,0]:
            img = new_list[2]
        if fingerup == [0, 1, 1, 1, 0] and fingers_up==[0,0,0,0,0] :
            img = new_list[3]
        if fingerup == [0, 1, 1, 1, 1] and fingers_up==[0,0,0,0,0] :
            img = new_list[4]
        if fingerup == [1, 1, 1, 1, 1] and fingers_up==[0,0,0,0,0] :
            img = new_list[5]
        if fingers_up == [0, 1, 0, 0, 0] and fingerup == [1, 1, 1, 1, 1]:
            img = new_list[6]
        if fingers_up == [0, 1, 1, 0, 0] and fingerup == [1, 1, 1, 1, 1]:
            img = new_list[7]
        if fingers_up == [0, 1, 1, 1, 0] and fingerup == [1, 1, 1, 1, 1]:
                img = new_list[8]
        if fingers_up == [0, 1, 1, 1, 1] and fingerup == [1, 1, 1, 1, 1]:
            img = new_list[9]
        if fingers_up == [1, 1, 1, 1, 1] and fingerup == [1, 1, 1, 1, 1]:
            img = new_list[10]
        resized_image = cv2.resize(img, (200, 200))
        frame[0:200, 0:200] = resized_image

    ctime = time.time()
    # The frames per second: fps
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(frame, f'FPS:{int(fps)}', (200, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
    cv2.imshow("window", frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()

