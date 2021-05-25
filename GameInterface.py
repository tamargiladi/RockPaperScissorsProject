import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
# import tkinter as tk
import GameSpace as GS
import mediapipe as mp
import os
import time
import HandTrackingModule as htm
import matplotlib.pyplot as plt


playerScore = 0
playerMove = " "
computerScore = 0
computerMove = " "
labelWidth = 20
Color = 'aqua'
status = "Not ready!"  # (Not ready/Ready) get this from the gameSpace

def fingerDetect():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    wCam, hCam = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    detector = htm.handDetector(detectionCon=0.75)

    pTime = 0
    cTime = 0

    tipIds = [4, 8, 12, 16, 20]
    t = 0
    while (t < 1):
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)
        statusLabel.configure(text="Ready!")   # changing status in interface to Ready
        start.config(state="disable")
        root.update()                          # changing status in interface to Ready
        if len(lmList) != 0:
            fingers = []
            t += 1
            # Thumb
            if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:  # [2] is Y
                    fingers.append(1)
                else:
                    fingers.append(0)

            # print(fingers)
            totalFingers = fingers.count(1)

         #   playerMoveLabel.text = StringVar()
            if totalFingers==5:
                playerMoveLabel.configure(text="Paper")
            elif totalFingers==0:
                playerMoveLabel.configure(text="Rock")
            else:
                playerMoveLabel.configure(text="Scissors")
            statusLabel.configure(text="Not ready!")
            start.config(state="normal")
            root.update()
            print(totalFingers)


            #    h, w, c = overlayList[0].shape # take the size of the image
            #    img[0:h, 0,w] = overlayList[0]   # pleace the image of finger in the left upper corrner

        # cv2.imshow("Image", img)
        cv2.waitKey(1)


root = Tk()
root.title("Rock Paper Scissors")
root.configure(background=Color)
# root.geometry("400x400")


statusLabel = Label(root, text=status, pady=50, font=("Helvetica", 15), background=Color)
statusLabel.grid(row=0, column=0, columnspan=2)

computerMoveFrame = LabelFrame(root, text="Computer move", borderwidth=3, padx=30, pady=50, font=("Helvetica", 15),
                               background=Color)
computerMoveFrame.grid(row=1, column=0)
computerMoveLabel = Label(computerMoveFrame, text=computerMove, width=labelWidth, padx=10, pady=10,
                          font=("Helvetica", 20))
computerMoveLabel.pack()

playerMoveFrame = LabelFrame(root, text="Player Move", borderwidth=3, padx=30, pady=50, font=("Helvetica", 15),
                             background=Color)
playerMoveFrame.grid(row=1, column=1)
playerMoveLabel = Label(playerMoveFrame, text=playerMove, width=labelWidth, padx=10, pady=10, font=("Helvetica", 20))
playerMoveLabel.pack()

computerScoreFrame = LabelFrame(root, text="Computer Score", borderwidth=3, padx=30, pady=50, font=("Helvetica", 15),
                                background=Color)
computerScoreFrame.grid(row=2, column=0)
computerScoreLabel = Label(computerScoreFrame, text=computerScore, width=labelWidth, padx=10, pady=10,
                           font=("Helvetica", 20))
computerScoreLabel.pack()

playerScoreFrame = LabelFrame(root, text="Player Score", borderwidth=3, padx=30, pady=50, font=("Helvetica", 15),
                              background=Color)
playerScoreFrame.grid(row=2, column=1)
playerScoreLabel = Label(playerScoreFrame, text=playerScore, width=labelWidth, padx=10, pady=10, font=("Helvetica", 20))
playerScoreLabel.pack()

start = Button(root, text="Start", command=fingerDetect, borderwidth=3, padx=50, pady=10, font=("Helvetica", 15))
start.grid(row=3, column=0, columnspan=2, pady=50)

root.mainloop()

