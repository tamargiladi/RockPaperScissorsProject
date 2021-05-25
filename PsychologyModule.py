import random

#p - The player
#c - The computer

arr = ['Rock','Paper','Scissors']



# Return the throw that would lose to action
def loser_action(action):
    if action == 'Rock':
        return 'Scissors'
    elif action =='Paper':
        return 'Rock'
    else:
        return 'Paper'

def winner_action(action):
    if action =='Rock':
        return 'Scissors'
    elif action =='Paper':
        return 'Rock'
    else:
        return 'Paper'


def non_dependent_partial_guess():
    return random.choices(arr, weights=[0.354,0.350,0.296])[0]

#Changes due to strategy
def depndent_if_repeated(p1,p2):
    print("depndent_if_repeated")

    if p1==p2:
        return True, loser_action(p1)

    return False,-1

#TOOD MOSHE - HERE WRITE FUNCTION



for i in range(10):
    print(non_dependent_partial_guess())