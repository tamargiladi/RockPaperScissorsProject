import cv2
import FingerCoutnerModule as htm
import SingleGame
import numpy as np
import GameInterface as GI


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
        #TODO: Function that recognize hand type
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

#====The game operation
while countGame<100:
    operate = True
    while operate:
        print(countGame)
        success, img =cap.read()
        edges = cv2.Canny(img, 100, 200)
        img = detector.findHands(img)

        right_space = 920

        lmList_left = detector.findPosition(img, draw=False)

        handType,fingerCounter,running = detector.countSingle(lmList=lmList_left)

        if(fingerCounter==-2):
            cv2.putText(img, "NO HANDS", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                        text_color_hands, 3)
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


            g = SingleGame.Game(player=action)
            g_winner, g_action = g.computerPlay()


            if g_winner:
                result.append(g_winner)



            operate = False

    # TODO: OPERATION OF HAND!
    #     # ========================================
    #     #     HAND OPERATION GOES HERE
    #     # ========================================

    cv2.waitKey(100)
    countGame = countGame + 1
    if running == False and count<4:
        running = True
        ("STOP STOP STOP STOP STOP")
        count = count + 1
    elif running==True and count<100:
        count = 0

    #cv2.imshow("Image", img)
    gi = GI.GameWindow("player")
    cv2.imshow("Image",gi.createWindow())
    cv2.waitKey(1)
    #print(handType,fingerCounter,running)
    #detector.findPositionMultiple()

computerScore =  result.count('computer')
playerScore = result.count('player')


print(result)
print("BIG WINNER:",end="")
if(computerScore>playerScore):
    print("computer!!")
    #Winner V
elif (playerScore>computerScore):
    print("YOU!")
    #GOOD SPORT, ONE THUMB
else:
    print("TIE")
    #Shake hand

#Computer makes funny gesture on winning and on lost

# img[:,:] = text_color_count
# img_close = cv2.imread("images_other/Close.png")
# img[150:img_close.shape[0]+150,800:img_close.shape[1]+800]=img_close
#
# cv2.putText(img, "GOODBYE!", (70, 400), cv2.FONT_HERSHEY_TRIPLEX, 4,
#                 text_color_hands, 10)
# cv2.imshow("Image", img)



#========= GAME GAME GAME=========#


