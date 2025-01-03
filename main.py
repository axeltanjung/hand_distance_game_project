import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
import cvzone

# Open Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Find function
# X is the distance between the thumb and the index finger

x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2)

# Looping
while True:
    success, img = cap.read()
    hand, img = detector.findHands(img, draw=False)

    if hands:
        lmList = hands[0]['lmList']
        x, y, w, h = hands[0]['bbox']
        x1, y1 = lmList[5]
        x2, y2 = lmList[17]

        distance = int(math.sqrt((y2-y1)**2 + (x2-x1)**2))
        A, B, C = coff
        distanceCM = A*distance**2 + B*distance + C

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x1, y1, x2, y2), 2, 2)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)