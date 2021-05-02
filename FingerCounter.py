import cv2
import FingerCoutnerModule as htm
import GamePy


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


while countGame<100:
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


        g = GamePy.Game(player=action)

        g.computerPlay()
        cv2.waitKey(1000)




    if running == False and count<4:
        running = True
        ("STOP STOP STOP STOP STOP")
        count = count + 1
    elif running==True and count<100:
        count = 0

    cv2.imshow("Image", img)

    cv2.waitKey(1)
    #print(handType,fingerCounter,running)
    #detector.findPositionMultiple()



img[:,:] = text_color_count
img_close = cv2.imread("images_other/Close.png")
img[150:img_close.shape[0]+150,800:img_close.shape[1]+800]=img_close

cv2.putText(img, "GOODBYE!", (70, 400), cv2.FONT_HERSHEY_TRIPLEX, 4,
                text_color_hands, 10)
cv2.imshow("Image", img)



#========= GAME GAME GAME=========#


