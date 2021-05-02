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
    def __init__(self, player):
        self.player = player
    def computerPlay(self):
        count = 0
        print("player:", self.player)

        actions = ["Rock", "Paper", "Scissors"]
        actionsCount = [0,0,0]
        score_player, score_computer = 0, 0
        if self.player!="INVALID ACTION":
            while score_player==0 and score_computer==0 and count<4000:
                computer = random.choices(actions)[0]
                if self.player != computer:
                    if self.player == "Rock":
                        # Player wins
                        if computer == "Scissors":
                            score_player = score_player + 1
                        elif computer == "Paper":
                            score_computer = score_computer + 1
                            actionsCount[1] = actionsCount[1]+1
                    elif self.player == "Scissors":
                        if computer == "Paper":
                            score_player = score_player + 1
                        elif computer == "Rock":
                            score_computer = score_computer + 1
                            actionsCount[0] = actionsCount[0]+1

                    # player is playing paper
                    else:
                        if computer == "Rock":
                            score_player = score_player + 1
                        elif computer=="Scissors":
                            score_computer = score_computer + 1
                            actionsCount[2] = actionsCount[2]+1


                count = count + 1
            #print("GOOD:",actions[actionsCount.sort()[2]])
            cv2.waitKey(1)

            if score_computer > score_player:
                print("COMPUTER WINS!" , computer , " beats ", self.player)
            elif score_computer < score_player:
                print("YOU WIN!", self.player , " beats ", computer)
            else:
                print("TIE")
        else:
            print("INVALID ACTION!!")