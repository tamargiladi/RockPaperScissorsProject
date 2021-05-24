import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import GameSpace as GS

#def updateLabel(num):
#    label.config(str(num))

# game = GS.GameProgress()

playerMove= "Rock"
playerScore = 0
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

