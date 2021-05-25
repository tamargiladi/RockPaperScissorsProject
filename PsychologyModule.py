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
        return 'Paper'
    elif action =='Paper':
        return 'Scissors'
    else:
        return 'Rock'


def non_dependent_partial_guess():
    return random.choices(arr, weights=[0.354,0.350,0.296])[0]


#Changes due to strategy
def depndent_if_repeated(p1,p2):
    print("depndent_if_repeated")

    if p1==p2:
        return True, loser_action(p1)

    return False,-1


#TOOD MOSHE - HERE WRITE FUNCTION
def last_winners_or_losser_wins_move(p1,c1):
    if loser_action(c1) == p1:      # If a player loses, he will make the move that wins the move he lost to him,
        return p1                   # therefore we will make a move that wins the move he made ---> and it's always the first move he made :)
    else
        return winner_action(p1)    # player wins or tie, therefore he continue to make the same move and we make move that wins the move he made



for i in range(10):
    print(non_dependent_partial_guess())