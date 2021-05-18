import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
#
#
# class GameWindow:
#     def __init__(self, winner):
#         self.winner = winner
#
#     def createWindow(self):
#       img = cv2.imread('images/4853433.jpg')
#
#       img[30:300,30:300] = (255,0,0)
#       font,org,fontScale,color,thickness = cv2.FONT_HERSHEY_SIMPLEX,(1500, 100),1, (255, 0, 0),2
#
#       # Using cv2.putText() method
#       img=  cv2.putText(img, 'OpenCV', org, font,
#                           fontScale, color, thickness, cv2.LINE_AA)
#
#
#       return img
#
#     def operateWindow(self, img):
#         cv2.imshow("Frame",img)
#         cv2.waitKey()
#
# #
# #
# # g = GameWindow("SOMERHING")
# #
# #
# g.operateWindow(g.createWindow())

class window:
    def __init__(self):
        self.root =Tk()
        self.score_computer_label = Label(self.root, text="0")


    def operate_root(self):
        self.score_computer_label.pack()
        self.root.mainloop()

    def change_computer_score(self, num):
        self.score_computer_label.config(text=str(num))


while True:
    #sdfdljkks











print("hello")