import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import numpy
# import tkinter as tk
# import GameSpace as GS
import mediapipe as mp
import os
import time
import HandTrackingModule as htm
import matplotlib.pyplot as plt
import PsychologyModule as PSYCH
from queue import Queue
import random
#import ExecuteHand as EH


MAX_ITERATIONS = 30
computerMove = " "
labelWidth = 20
Color = 'aqua'
status = "Not ready!"


before_screen = Tk()
class Counter:
    def __init__(self):
        self.value = 0
    def increase(self):
        self.value +=1
    def getValue(self):
        return self.value


class GameMoves:
    def __init__(self):
        self.computerMove = ""
        self.playerMove= ""



#A function that helps to find the correct fingers.
def does_contain(test_set,requiered_elements):
    return requiered_elements.issubset(test_set)


def find_correct_count(fingers_array,hand):

    if hand=="right":
        full_hand = 4
    else:
        full_hand = 5

        # All counts are identical
    if(len(set(fingers_array))==1):
        if fingers_array[0]==full_hand:
            return full_hand
        else:
            return fingers_array[0]

    else:
        set_fg= set(fingers_array)

        if does_contain(set_fg,{0,1}) or does_contain(set_fg,{0,1,4,5}) or does_contain(set_fg,{1,4,5}):
            return 0
        else:
            return most_frequent(fingers_array)





def rightHandMode():
    global handMode
    handMode = "right"
    before_screen.destroy()

def leftHandMode():
    global handMode
    handMode ="left"
    before_screen.destroy()


def most_frequent(List):
    if len(List)>0:

        counter = 0
        num = List[0]

        for i in List:
            curr_frequency = List.count(i)
            if (curr_frequency > counter):
                counter = curr_frequency
                num = i

        return num
    else:
        return -1

def fingerDetect():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    wCam, hCam = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    detector = htm.handDetector(detectionCon=0.75)  # we can play with value to adjust the tracking

    pTime = 0
    cTime = 0

    tipIds = [4, 8, 12, 16, 20]
    t = 0
    inside_iterations = 0
    total_fingers_count = []

    while (t < MAX_ITERATIONS):
        global final_count
        global playerMove
        # t += 1
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if t<MAX_ITERATIONS/4:
            statusLabel.configure(text="Show your hand")   # changing status in interface to Ready

        start.config(state="disable")
        root.update()                          # changing status in interface to Ready

        if len(lmList) != 0:
            fingers = []
            inside_iterations += 1
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

            if t>=int(MAX_ITERATIONS/4):

                statusLabel.configure(text="MOVE!")  # changing status in interface to Ready

                total_fingers_count.append(totalFingers)



         #   playerMoveLabel.text = StringVar()
         #    if handMode=="left":
         #        if totalFingers==5:
         #            playerMoveLabel.configure(text="Paper")
         #        elif totalFingers==0:
         #            playerMoveLabel.configure(text="Rock")
         #        else:
         #            playerMoveLabel.configure(text="Scissors")
         #    else:
         #        if totalFingers==5:
         #            playerMoveLabel.configure(text="Paper")
         #        elif totalFingers==0:
         #            playerMoveLabel.configure(text="Rock")
         #        elif totalFingers==2:
         #            playerMoveLabel.configure(text="Scissors")
         #        else:
         #            statusLabel.configure(text="try again")

            start.config(state="normal")
            root.update()
            # time.sleep(0.3)


            #    h, w, c = overlayList[0].shape # take the size of the image
            #    img[0:h, 0,w] = overlayList[0]   # pleace the image of finger in the left upper corrner

        # cv2.imshow("Image", img)
    cv2.waitKey(1)
    print(total_fingers_count)
    final_count = find_correct_count(total_fingers_count,handMode)
    print(final_count)
    print(handMode)

    if(final_count!=-1):
        if handMode == "left":
            if final_count == 5:
                playerMove = "Paper"
            elif final_count == 0:
                playerMove = "Rock"
            elif final_count==2:
                playerMove = "Scissors"
            else:
                playerMove =" "
        else:
            if final_count == 4:
                playerMove = "Paper"
            elif final_count == 0:
                playerMove = "Rock"
            else:
                playerMove="Scissors"
    else:
        playerMove=""

    hebrew_playerMove = ""

    if playerMove =="Paper":
        hebrew_playerMove="נייר"
    elif playerMove =="Rock":
        hebrew_playerMove ="אבן"
    else:
        hebrew_playerMove = "מספריים"

    print("PAST CONFIGURE?")
    print(pQ)

    if not pQ.full() and playerMove!=" ":
        if playerMove =="Rock":
            pQ.put("Rock")
        elif playerMove == "Paper":
            pQ.put("Paper")
        elif playerMove=="Scissors":
            pQ.put("Scissors")
        print("PAST pQ??")

    statusLabel.configure(text="")

    #The computer plays
    print("the computer is the problem")
    if counter.getValue() == 0:
        computer_action = "Paper"  # Most throw rock first time, therfore computer throw paper.
    elif counter.getValue() == 1:
        computer_action = PSYCH.non_dependent_partial_guess()
    else:
        # TODO Choose randomly between all the following methods
        #Random choice between stradegies
        choice = random.choice([0,1])
        if pQ.full():
            #Repeat stradegy
            if choice ==0:
                print("0")
                is_repeated_action,true_action = PSYCH.depndent_if_repeated(pQ.queue[0], pQ.queue[1])

                if not is_repeated_action:
                    computer_action = PSYCH.non_dependent_partial_guess()
                else:
                    computer_action = true_action
            #Psycholgy of winners or losers
            else:
                computer_action = PSYCH.last_winners_or_losser_wins_move(pQ.queue[1],cQ.queue[1])   # TODO:Write the psychological winning method - MOSHE
                # computer_action = PSYCH.non_dependent_partial_guess() #TODO REMOVE ME!


            pQ.get()
            cQ.get()
        else:
            computer_action = PSYCH.non_dependent_partial_guess()

    if not cQ.full():
        if computer_action == "Rock":
            cQ.put("Rock")
        elif computer_action == "Paper":
            cQ.put("Paper")
        elif computer_action == "Scissors":
            cQ.put("Scissors")


    hebrew_computerAction = ""

    if computer_action == "Paper":
        hebrew_computerAction = "נייר"
    elif computer_action == "Rock":
        hebrew_computerAction = "אבן"
    else:
        hebrew_computerAction = "מספריים"



    playerMoveLabel.configure(text=hebrew_playerMove)
    computerMoveLabel.configure(text=hebrew_computerAction)
    if (computer_action == 'Rock'):
        print("doRock()")
        # EH.doRock()
    elif (computer_action == 'Scissors'):
        print("doScissors()")
        # EH.doScissors()
    elif (computer_action == 'Paper'):
        print("doPaper()")
        # EH.doPaper()
    start.config(state="normal")
    counter.increase()

    if PSYCH.loser_action(playerMove)==computer_action:
        playerScore.increase()
    elif PSYCH.loser_action(computer_action)==playerMove:
        computerScore.increase()


    computerScoreLabel.config(text=str(computerScore.getValue()))
    playerScoreLabel.config(text=str(playerScore.getValue()))

countGame = 0
handMode = ""
MAX_ROUNDS =2
global computerScore


counter= Counter()
computerScore =Counter()
playerScore = Counter()
moves = GameMoves()

root = Tk()
pQ = Queue(maxsize=MAX_ROUNDS)
cQ = Queue(maxsize=MAX_ROUNDS)


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
playerMoveLabel = Label(playerMoveFrame, text="", width=labelWidth, padx=10, pady=10, font=("Helvetica", 20))
playerMoveLabel.pack()

computerScoreFrame = LabelFrame(root, text="Computer Score", borderwidth=3, padx=30, pady=50, font=("Helvetica", 15),
                                background=Color)
computerScoreFrame.grid(row=2, column=0)
computerScoreLabel = Label(computerScoreFrame, text="0", width=labelWidth, padx=10, pady=10,
                           font=("Helvetica", 20))
computerScoreLabel.pack()

playerScoreFrame = LabelFrame(root, text="Player Score", borderwidth=3, padx=30, pady=50, font=("Helvetica", 15),
                              background=Color)
playerScoreFrame.grid(row=2, column=1)
playerScoreLabel = Label(playerScoreFrame, text="0", width=labelWidth, padx=10, pady=10, font=("Helvetica", 20))
playerScoreLabel.pack()

start = Button(root, text="Start", command=fingerDetect, borderwidth=3, padx=50, pady=10, font=("Helvetica", 15))
start.grid(row=3, column=0, columnspan=2, pady=50)


root.eval('tk::PlaceWindow . center')

right_button = Button(before_screen, text="RIGHT", command = rightHandMode, borderwidth=3, padx=50,
                       pady=10, font=("Helvetica", 15))

right_button.grid(row=0, column=0, columnspan=2, pady=0)


left_button = Button(before_screen, text="LEFT", command = leftHandMode, borderwidth=3, padx=50,
                       pady=10, font=("Helvetica", 15))

left_button.grid(row=1, column=0, columnspan=1, pady=0)

before_screen.mainloop()


root.mainloop()
