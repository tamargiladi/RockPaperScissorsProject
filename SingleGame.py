import random
import cv2
import numpy as np


def beaten_action(action):
    if action == "Rock":
        return "Paper"
    elif action =="Paper":
        return "Scissors"
    else:
        return "Rock"

def winner_action(action):
    if action =="Rock":
        return "Scissors"
    elif action =="Paper":
        return "Rock"
    else:
        return "Paper"

class Game:
    def __init__(self, player,computer):
        self.player = player
        self.computer = computer

    def computerPlay(self):
        winner, winner_action = "", ""
        count = 0


        actionsCount = [0,0,0]
        score_player, score_computer = 0, 0
        if self.player!="INVALID ACTION":
            if self.player != self.computer:
                if self.player == "Rock":
                    # Player wins
                    if self.computer == "Scissors":
                        score_player = score_player + 1
                    elif self.computer == "Paper":
                        score_computer = score_computer + 1
                        actionsCount[1] = actionsCount[1]+1
                elif self.player == "Scissors":
                    if self.computer == "Paper":
                        score_player = score_player + 1
                    elif self.computer == "Rock":
                        score_computer = score_computer + 1
                        actionsCount[0] = actionsCount[0]+1

                # player is playing paper
                else:
                    if self.computer == "Rock":
                        score_player = score_player + 1
                    elif self.computer=="Scissors":
                        score_computer = score_computer + 1
                        actionsCount[2] = actionsCount[2]+1

            # cv2.waitKey(1)

            if score_computer > score_player:
                winner = "computer"
            elif score_computer < score_player:
                winner =  "player"
            else:
               winner =  "tie"
        else:
            winner = "invalid"

        if winner!="invalid":
            if winner == "player":
                return winner, self.player
            elif winner == "computer":
                return winner, self.computer
            else:
                return "none","none"
        else:
            return "none","none"