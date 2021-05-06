import cv2
import numpy as np
import matplotlib.pyplot as plt


class GameWindow:
  def __init__(self, winner):
    self.winner = winner

  def createWindow(self):
      img = cv2.imread('images/4853433.jpg')
      cv2.imshow("Game",img)

      cv2.waitKey()


g = GameWindow("SOMERHING")

g.createWindow()