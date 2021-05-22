import cv2
import FingerCoutnerModule as htm
import SingleGame
import modelML as ML
import tkinter as tk
from tkinter import ttk
import time
import fingersCount as FC
class App(tk.Tk):
    def __init__(self):
        super().__init__()


        self.title('Rock Pape Scissors Game')
        self.style = ttk.Style(self)
        self.text = ttk

        self.button = ttk.Button(self, text='Wait 3 seconds')
        self.text = ttk.text(self,text="Player score")
        self.button['command'] = self.change_button_text("try")
        self.button.pack(expand=True, ipadx=10, ipady=5)
        self.text.pack()

    def start(self):
        self.change_button_color('red')
        time.sleep(3)
        self.change_button_color('black')

    def change_button_color(self, color):
        self.style.configure('TButton', foreground=color)
    def change_button_text(self, text):
        self.button.configure(text="hello")

from threading import Thread

numOfHands_tmp = 1
handType_tmp = "Left"

thumbLeft_tmp, thumbRight_tmp = True, False
numOfFingers_tmp = 3
#==============

class GameProgress:
    def __init__(self, player_move,computer_move,score_computer=0,score_player=0):
        self.player_move = player_move
        self.computer_move = computer_move
        self.score_computer = score_computer
        self.score_player = score_player

    def get_player_move(self):
        return self.player_move

    def get_computer_move(self):
        return self.computer_move

    def get_score_player(self):
        return self.score_player

    def get_score_computer(self):
        return self.score_computer


# #=======FUNCTIONS SECTION=================
# def checkSingleGesture(fingers_list, thumb):
#
#     down_fingers =  (fingers_list["Ring"] is False) and (fingers_list["Middle"] is False)
#     up_fingers = fingers_list["Index"] and fingers_list["Pinky"] and  thumb
#
#     return down_fingers and up_fingers
#
# def specialDetect():
#     #multi_hand_landmarks
#     #MULTI_HANDEDNESS
#
#     num_of_hands = numOfHands_tmp
#
#
#     if(num_of_hands>1):
#         return "Both"
#     else:
#
#         hand_type = "Left"
#             #Here function...
#
#         hand_type = handType_tmp
#
#         return hand_type
#
# def countSingle(handType):
#
#     fingers_list = {"Pinky":True,"Ring":False,
#                     "Middle":False,"Index":True}
#
#     thumb = False
#
#
#
#     #TODO: Calculate number of all fingers except thumb
#     #Your code
#
#     num_of_fingers = numOfFingers_tmp
#
#
#
#
#     #====THUMB CACLUALTION=====#
#
#     if(handType=="Left"):
#         #TODO: Function that calculates thumb of left hand
#         #Your code here
#         thumb = thumbLeft_tmp
#
#     else:
#         #TODO: Function that calcualtes thumb of right hand
#         #Your code here...
#         thumb = thumbRight_tmp
#
#
#     return num_of_fingers, checkSingleGesture(fingers_list,thumb)


def operate():
    for i in range(12):
        print("ENTERED!")
    #todo:
    #  remove later !!!!
    printed =False

    # todo================
    text_color_hands = (0,69,255)
    text_color_count = (209,206,0)


    #Determines if the program should continue or not
    running, countLeft, countRight = True,0,0

    # detector = htm.handDetector(detectionCon=0.75)


    KNN = ML.KNN_train(ML.get_table())
    table_ML = ML.create_results_table()

    #print(table_ML)


    #Video conf



    action = ""

    ind_table = 0
    countGame = 0

    computerScore = 0
    playerScore = 0



    last_computer_action = ""
    permitted_actions = [0,2,5]
    for count in range(10):
        while countGame<10:
            print("GO")

            #--START---The single game operation

            fg.startLoop()
            #>>>>Camera detection
            fingerCounter = fg.getCount()


            #  #Calculates actions of the user
            # if(fingerCounter==-2):
            #     # cv2.putText(img, "NO HANDS", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
            #     #             text_color_hands, 3)
            #     running = True
            # else:
            #     if fingerCounter==0:
            #         action = "Rock"
            #     elif fingerCounter==4:
            #         action = "Paper"
            #     else:
            #         action = "Scissors"
            if fingerCounter in permitted_actions:
                if fingerCounter == 0:
                    action = "Rock"
                elif fingerCounter == 5:
                    action = "Paper"
                elif fingerCounter == 2:
                    action = "Scissors"


                last_player_action = action







                #MACHINE LEARNING ALGORITHMS OR PSYCHOLOGY ALGORITHM

                if (countGame+1) % 3 != 0:
                    if (countGame+1) %3==1 and countGame!=0:
                        ind_table = ind_table+1      # increases table index when reaching to new triple game
                    if countGame!=0:
                        computer_action = SingleGame.psychology_beat(last_player_action,last_computer_action)
                        last_computer_action = computer_action
                    else:
                        computer_action = "Paper"
                        last_computer_action = "Paper"
                    computer_action_NUM = ML.action_to_number(computer_action)
                    action_NUM = ML.action_to_number(action)

                    computer_action = ML.number_to_action(ML.KNN_prediction(table_ML, KNN)[ind_table])
                    # print(int(action_NUM), int(computer_action_NUM), countGame, ind_table,
                    #                                        table_ML)
                    table_ML = ML.update_results_table(int(action_NUM), int(computer_action_NUM), countGame, ind_table,
                                                           table_ML)

                else:
                    # computer_action = ML.number_to_action()
                    predicted_player_action = int(ML.KNN_prediction(table_ML, KNN)[ind_table])
                    # print(ML.number_to_action(predicted_player_action))
                    computer_action = SingleGame.beat_action(ML.number_to_action(predicted_player_action))



                # TODO: Saving database of

                #=======KEEP OUT
                #TODO: EXECUTE HAND HERE
                #=======KEEP OUT
                if action != "INVALID ACTION":
                    g_winner= SingleGame.is_winner(int(ML.action_to_number(action)),int(ML.action_to_number(computer_action)))
                    winner = ""
                    if g_winner==1:
                        winner = "player"
                    elif g_winner==-1:
                        winner = "computer"
                    else:
                        winner= "tie"

                    if winner == "computer":
                        computerScore = computerScore + 1
                    elif winner == "player":
                        playerScore = playerScore + 1

                    print("winner:",winner ,"player action:",action , "  computer action:", computer_action)


                    countGame = countGame + 1
                    time.sleep(3)




        countGame = 0

        print("========")
        # print(ML.KNN_prediction(table_ML,KNN))
        # print("player score:",playerScore,"computer score:", computerScore)
        playerScore = 0
        computerScore=0




def something():
    print("afhjkds")


if __name__ == "__main__":
    # app = App()
    # app.mainloop()
    fg = FC.Fingers()

    operate()