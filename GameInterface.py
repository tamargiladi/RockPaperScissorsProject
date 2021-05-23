import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import GameSpace as GS







#def updateLabel(num):
#    label.config(str(num))

root = Tk()
root.title("Rock Paper Scissors")
computerLabel = Label(root, text="Computer", padx=40, pady=20) #columnspan=3
playerLabel = Label(root, text="Player", padx=40, pady=20)

computerLabel.grid(row=0, column=0)
playerLabel.grid(row=0, column=1)

root.mainloop()

#root.after(0, GS.operate())
#label.pack()

