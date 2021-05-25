"""
Hand Tracing Module
By: Murtaza Hassan
Youtube: http://www.youtube.com/c/MurtazasWorkshopRoboticsandAI
Website: https://www.murtazahassan.com/
"""

import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):

        lmList = []

        #Chooses the correct hand
        if self.results.multi_hand_landmarks:
            handsNum = len(self.results.multi_hand_landmarks)

            if(handsNum==1):
                #print(self.results.multi_hand_landmarks[0])
                #print(self.results.multi_handedness[0].classification[0].label)
                #print(len(self.results.multi_handedness))

                statement = self.results.multi_handedness[0].classification[0].label=="Left"
                #print(self.results.multi_handedness[0].classification[0].label)

                myHand = self.results.multi_hand_landmarks[0]
            else:
                #print(len(self.results.multi_handedness),self.results.multi_handedness[0])

                if(self.results.multi_handedness[0].classification[0].label=="Left"):
                    myHand = self.results.multi_hand_landmarks[0]
                else:
                    myHand = self.results.multi_hand_landmarks[1]


            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList


    def countSingle(self,lmList):
        hand_type, count_fingers = "No detection", -2

        fingerState = {"Thumb":False,"Index":False,"Middle":False,"Ring":False, "Pinky":False}
        if self.results.multi_hand_landmarks:
            # ====HAND TYPE====
            if len(self.results.multi_hand_landmarks)==1:
                count_fingers = 0
                hand_label = self.results.multi_handedness[0].classification[0].label
                if hand_label =="Left":
                    hand_type="Left"
                else:
                    hand_type="Right"

                #====FINGERS COUNT====
                fingerArr = [["Pinky", 20, 18], ["Ring", 16, 14], ["Middle", 12, 10], ["Index", 8, 6], ["Thumb", 4, 5]]

                for finger in fingerArr:
                    fingerName, fingerUp, fingerLow = finger[0], finger[1], finger[2]

                    if fingerName != "Thumb":
                        statement = lmList[fingerUp][2] < lmList[fingerLow][2]

                        if statement:
                            count_fingers = count_fingers + 1
                            fingerState[fingerName] = True



            else:
                hand_type="BOTH"
                count_fingers=-1

        if hand_type == "Left":
            hand_type="Right"
        elif hand_type== "Right":
            hand_type = "Left"

        running_state_down = fingerState["Middle"] is False and fingerState["Ring"] is False
        running_state_up = fingerState["Thumb"] and fingerState["Pinky"] and fingerState["Index"]




        return hand_type, count_fingers, not (running_state_down and running_state_up)

