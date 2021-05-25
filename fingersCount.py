import cv2
import time
import os
import HandTrackingModule as htm
from queue import LifoQueue


class Fingers():
    def __init__(self):
        self.countFingers = 0
        self.S = LifoQueue(maxsize =20)
    def startLoop(self):

        wCam, hCam = 640, 480

        cap = cv2.VideoCapture(0)
        cap.set(3, wCam)
        cap.set(4, hCam)

        pTime = 0

        prev_val = 0
        countFingers = 0
        countIt, notChanged = 0, True
        detector = htm.handDetector(detectionCon=0.75)
        condition = True
        tipIds = [4, 8, 12, 16, 20]


        while not self.S.full():
            success, img = cap.read()
            if success:
                img = detector.findHands(img)
                lmList = detector.findPosition(img, draw=False)
                # print(lmList)

                if len(lmList) != 0:
                    fingers = []

                    # Thumb
                    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                    # 4 Fingers
                    for id in range(1, 5):
                        if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                            fingers.append(1)
                        else:
                            fingers.append(0)
                    self.S.put(fingers.count(1))


                cv2.waitKey(1)





    def getCount(self):
        val =  self.S.get()

        #Value we wanted recived. Now we can empty the stack for new iteration

        while not self.S.empty():
            self.S.get()

        return val