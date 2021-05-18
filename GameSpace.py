import cv2
import FingerCoutnerModule as htm
import SingleGame
import random
import ExecuteHand
import numpy as np
# import GameInterface as GI
# import ExecuteHand as EH

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




#=======FUNCTIONS SECTION=================
def checkSingleGesture(fingers_list, thumb):

    down_fingers =  (fingers_list["Ring"] is False) and (fingers_list["Middle"] is False)
    up_fingers = fingers_list["Index"] and fingers_list["Pinky"] and  thumb

    return down_fingers and up_fingers

def specialDetect():
    #multi_hand_landmarks
    #MULTI_HANDEDNESS

    num_of_hands = numOfHands_tmp


    if(num_of_hands>1):
        return "Both"
    else:

        hand_type = "Left"
            #Here function...

        hand_type = handType_tmp

        return hand_type

def countSingle(handType):

    fingers_list = {"Pinky":True,"Ring":False,
                    "Middle":False,"Index":True}

    thumb = False



    #TODO: Calculate number of all fingers except thumb
    #Your code

    num_of_fingers = numOfFingers_tmp




    #====THUMB CACLUALTION=====#

    if(handType=="Left"):
        #TODO: Function that calculates thumb of left hand
        #Your code here
        thumb = thumbLeft_tmp

    else:
        #TODO: Function that calcualtes thumb of right hand
        #Your code here...
        thumb = thumbRight_tmp







    return num_of_fingers, checkSingleGesture(fingers_list,thumb)



#REMOVE LATER
numOfHands_tmp = 1
handType_tmp = "Left"

thumbLeft_tmp, thumbRight_tmp = True, False
numOfFingers_tmp = 3
#==============


text_color_hands = (0,69,255)
text_color_count = (209,206,0)




#Determines if the program should continue or not
running, countLeft, countRight = True,0,0

detector = htm.handDetector(detectionCon=0.75)


#Video conf
cap = cv2.VideoCapture(0)


action = ""

prev_left_count, prev_right_count =0 ,0
count = 0
countGame = 0
result = []
#
# ng = GI.window()
#
# ng.operate_root()

#====The game operation


while countGame<1:

    #--START---The single game operation
    operate = True

    while operate:


        #>>>>Camera detection
        success, img =cap.read()
        edges = cv2.Canny(img, 100, 200)
        img = detector.findHands(img)

        lmList = detector.findPosition(img, draw=False)
        handType,fingerCounter,running = detector.countSingle(lmList=lmList)

        #TODO: MACHINE LEARNING ALGORITHMS OR PSYCHOLOGY ALGORITHM
        #TODO: Saving database of

        #Calculates actions of the user
        if(fingerCounter==-2):
            # cv2.putText(img, "NO HANDS", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
            #             text_color_hands, 3)
            running = True
        else:
            if fingerCounter==0:
                action = "Rock"
            elif fingerCounter==2:
                action = "Scissors"
            elif fingerCounter==5:
                action = "Paper"
            else:
                action = "INVALID ACTION"

            cv2.putText(img, action, (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                        text_color_hands, 3)

         #   print(action)

            # ====Start random

            my_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
            action_computer = my_dict[random.randint(1,3)] #Random
           # print (action_computer)


            g = SingleGame.Game(player=action,computer=action_computer)

             #TODO: EXECUTE HAND HERE

            if (action_computer == 'Rock'):
                ExecuteHand.doRock()
            elif (action_computer == 'Scissors'):
                ExecuteHand.doScissors()
            elif (action_computer == 'Paper'):
                ExecuteHand.doPaper()

            g_winner, g_action = g.computerPlay()

            print (g_winner)

            operate = False


    # ng.change_computer_score(result.count("computer"))

    cv2.waitKey(100)
    countGame = countGame + 1

computerScore =  result.count('computer')
playerScore = result.count('player')


# print(result)
# print("BIG WINNER:",end="")
# if(computerScore>playerScore):
#     print("computer!!")
#     #Winner V
# elif (playerScore>computerScore):
#     print("YOU!")
#     #GOOD SPORT, ONE THUMB
# else:
#     print("TIE")
#     #Shake hand
#
# #Computer makes funny gesture on winning and on lost

# img[:,:] = text_color_count
# img_close = cv2.imread("images_other/Close.png")
# img[150:img_close.shape[0]+150,800:img_close.shape[1]+800]=img_close
#
# cv2.putText(img, "GOODBYE!", (70, 400), cv2.FONT_HERSHEY_TRIPLEX, 4,
#                 text_color_hands, 10)
# cv2.imshow("Image", img)



#========= GAME GAME GAME=========#


