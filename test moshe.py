import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import GameSpace as GS
import mediapipe as mp
import time
import os
import HandTrackingModule as htm
import matplotlib.pyplot as plt

#def updateLabel(num):
#    label.config(str(num))

# game = GS.GameProgress()

playerScore = 0
playerMove = "Rock"
computerScore = 0
computerMove = "Paper"
labelWidth = 20
Color = 'aqua'
status = "Not ready!"  # (Not ready/Ready) get this from the gameSpace

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# folderPath = "FingerImages"  # for showing finger images
# myList = os.listdir(folderPath)
# overlayList = []
# for imPath in myList:
#    image = cv2.imread(f'{folderPath}/{imPath}')
#    overlayList.append(image)

detector = htm.handDetector(detectionCon=0.75)
pTime = 0
cTime = 0
tipIds = [4, 8, 12, 16, 20]


root = Tk()
root.title("Rock Paper Scissors")
root.configure(background=Color)
# root.geometry("400x400")

#  while True:
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

start = Button(root, text="Start", command = root.update_idletasks(), borderwidth=3, padx=50, pady=10, font=("Helvetica", 15))
start.grid(row=3, column=0, columnspan=2, pady=50)


success, img = cap.read()
img = detector.findHands(img)
lmList = detector.findPosition(img, draw=False)
# print(lmList)
if len(lmList) != 0:
    fingers = []

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
        print(totalFingers)

        #    h, w, c = overlayList[0].shape # take the size of the image
        #    img[0:h, 0,w] = overlayList[0]   # pleace the image of finger in the left upper corrner

#        cv2.rectangle(img, (10, 10), (100, 120), (0, 255, 0), cv2.FILLED)
#        cv2.putText(img, str(totalFingers), (20, 105), cv2.FONT_HERSHEY_PLAIN, 7, (255, 0, 0), 15)

#    cTime = time.time()
#    fps = 1 / (cTime - pTime)
#    pTime = cTime
#    cv2.putText(img, f'FPS: {int(fps)}', (250, 70), cv2.FONT_HERSHEY_PLAIN, 3, (200, 0, 0), 3)

#    cv2.imshow("Image", img)
#    cv2.waitKey(1)

root.mainloop()

"""
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:  

  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
cv2.destroyAllWindows() 






playerMove= "Rock"
computerScore = 0
computerMove= "Paper"
labelWidth = 20
Color = 'aqua'
game = GS.GameProgress()
status = "Not ready!"  # (Not ready/Ready) get this from the gameSpace

root = Tk()
root.title("Rock Paper Scissors")
root.configure(background=Color)
#root.geometry("400x400")




statusLabel = Label(root, text=status, pady=50, font=("Helvetica", 15), background=Color)
statusLabel.grid(row=0, column=0, columnspan=2)

computerMoveFrame = LabelFrame(root, text="Computer move", borderwidth=3, padx=30, pady=50, font=("Helvetica", 15), background=Color)
computerMoveFrame.grid(row=1, column=0)
computerMoveLabel = Label(computerMoveFrame, text=game.get_computer_move(), width=labelWidth, padx=10, pady=10, font=("Helvetica", 20))
computerMoveLabel.pack()

playerMoveFrame = LabelFrame(root, text="Player Move", borderwidth=3, padx=30, pady=50, font=("Helvetica", 15), background=Color)
playerMoveFrame.grid(row=1, column=1)
playerMoveLabel = Label(playerMoveFrame, text=playerMove, width=labelWidth, padx=10, pady=10, font=("Helvetica", 20))
playerMoveLabel.pack()

computerScoreFrame = LabelFrame(root, text="Computer Score", borderwidth=3, padx=30, pady=50, font=("Helvetica", 15), background=Color)
computerScoreFrame.grid(row=2, column=0)
computerScoreLabel = Label(computerScoreFrame, text=computerScore, width=labelWidth, padx=10, pady=10, font=("Helvetica", 20))
computerScoreLabel.pack()


playerScoreFrame = LabelFrame(root, text="Player Score", borderwidth=3, padx=30, pady=50, font=("Helvetica", 15), background=Color)
playerScoreFrame.grid(row=2, column=1)
playerScoreLabel = Label(playerScoreFrame, text=playerScore, width=labelWidth, padx=10, pady=10, font=("Helvetica", 20))
playerScoreLabel.pack()


start = Button(root, text="Start", borderwidth=3, padx=50, pady=10, font=("Helvetica", 15))
start.grid(row=3, column=0, columnspan=2, pady=50)


#game.operate()

root.mainloop()

#root.after(0, GS.operate())
#label.pack()

"""