import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import GameSpace as GS

def updateLabel(num):
    label.config(str(num))

root = Tk()
label = Label(root,text="0")


root.after(0, GS.operate())
label.pack()

