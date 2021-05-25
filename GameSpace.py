import cv2
import FingerCoutnerModule as htm
import SingleGame
import modelML as ML
import tkinter as tk
from tkinter import ttk
import time
import fingersCount as FC
# import ExecuteHand as EH
import PsychologyModule as PSYCH
from queue import Queue

MAX_ROUNDS = 2

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


def operate():




    #Saves the action of the player every game
    action = ""

    ind_table = 0
    countGame = 0

    computerScore = 0
    playerScore = 0



    last_computer_action = ""


    pQ = Queue(maxsize=MAX_ROUNDS)
    cQ = Queue(maxsize=MAX_ROUNDS)

    permitted_actions = [0,2,5]

    for count in range(10):
        while countGame<10:
            computer_action = ""
            print("GO")

            #--START---The single game operation

            #>>>>Camera detection
            fg.startLoop()


            fingerCounter = fg.getCount()

            if fingerCounter in permitted_actions:
                if fingerCounter == 0:
                    action = "R"
                elif fingerCounter == 5:
                    action = "P"
                elif fingerCounter == 2:
                    action = "S"

                # if (countGame+1) % 3 != 0:
                #     if (countGame+1) %3==1 and countGame!=0:
                #         ind_table = ind_table+1      # increases table index when reaching to new triple game
                #     if countGame!=0:
                #         computer_action = SingleGame.psychology_beat(last_player_action,last_computer_action)
                #         last_computer_action = computer_action
                #     else:
                #         computer_action = "Paper"
                #         last_computer_action = "Paper"
                #     computer_action_NUM = ML.action_to_number(computer_action)
                #     action_NUM = ML.action_to_number(action)
                #
                #     computer_action = ML.number_to_action(ML.KNN_prediction(table_ML, KNN)[ind_table])
                #     # print(int(action_NUM), int(computer_action_NUM), countGame, ind_table,
                #     #                                        table_ML)
                #     table_ML = ML.update_results_table(int(action_NUM), int(computer_action_NUM), countGame, ind_table,
                #                                            table_ML)
                #
                # else:
                #     # computer_action = ML.number_to_action()
                #     predicted_player_action = int(ML.KNN_prediction(table_ML, KNN)[ind_table])
                #     # print(ML.number_to_action(predicted_player_action))
                #     computer_action = SingleGame.beat_action(ML.number_to_action(predicted_player_action))

                if countGame==0:
                    computer_action = "P" #Most throw rock first time, therfore computer throw paper.
                elif countGame==1:
                    computer_action = PSYCH.non_dependent_partial_guess()
                else:
                    #TODO Choose randomly between all the following methods

                    _,computer_action = PSYCH.depndent_if_repeated(pQ.queue[0],pQ.queue[1])




                # TODO: Saving database of

                #=======KEEP OUT

                if (computer_action == 'R'):
                    print("doRock()")
                    # EH.doRock()
                elif (computer_action == 'S'):
                    print("doScissors()")
                    # EH.doScissors()
                elif (computer_action == 'P'):
                    print("doPaper()")
                    # EH.doPaper()


                if action != "INVALID ACTION":
                    g_winner= SingleGame.is_winner(action,int(ML.action_to_number(computer_action)))
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


                    #Round over actions
                    if pQ.full() and pQ.full():
                        pQ.get()
                        cQ.get()

                    #Inserts the new move to the queues.
                    pQ.put(action)
                    cQ.put(action)


                    countGame = countGame + 1
                    time.sleep(1)




        countGame = 0

        print("========")
        # print(ML.KNN_prediction(table_ML,KNN))
        # print("player score:",playerScore,"computer score:", computerScore)
        playerScore = 0
        computerScore=0




if __name__ == "__main__":
    # app = App()
    # app.mainloop()
    fg = FC.Fingers()

    operate()