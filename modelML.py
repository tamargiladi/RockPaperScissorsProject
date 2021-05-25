import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn import tree

from sklearn.naive_bayes import GaussianNB

import time

import ModelMLModule as ML_DATA

#
# def prediction_NB(X_train, X_test, y_train):
#     gnb = GaussianNB()
#     y_pred = gnb.fit(X_train, y_train).predict(X_test)
#


def KNN_train(X):
    print("X:",X)
    y = X["p1_i"]
    y = y.astype('int')
    X = X.drop(columns=["p2_i","p1_i","p2_i-2","p1_i-2"])

    TEST_SIZE = 0.1
    neigh = KNeighborsClassifier(n_neighbors=int(np.sqrt(TEST_SIZE*X.shape[0])))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = TEST_SIZE, random_state = 0)

    print(X_train, y_train)
    neigh.fit(X_train, y_train)

    y_pred = neigh.predict(X_test)
    print("score:",neigh.score(X_test, y_test))

    return neigh

def KNN_prediction(X_test,knn,y_test):
    y_pred = knn.predict(X_test)
    print(knn.score(X_test, y_test))



    knn.score()
    return y_pred

def is_winner(p2,p1):

    #Rock - 1
    #Paper - 2
    #Scissors - 3


    if p2==1:
        if p1==3:
            return 1
        elif p1==2:
            return -1
        else:
            return 0
    elif p2==2:
        if p1==1:
            return 1
        elif p1==3:
            return -1
        else:
            return 0
    else:
        if p1==2:
            return 1
        elif p1==1:
            return -1
        else:
            return 0

def get_table():
    data = pd.read_csv("data/Rock_Paper_Scissors_Raw.csv")
    df = pd.DataFrame(data)

    df_final =ML_DATA.final_organize(df)
    # df_final['winner_1'] = None
    # df_final['winner_2'] = None
    # df_final['winner_3'] = None
    # #
    # # for ind in df_final.index:
    # #     df_final["winner_1"].values[ind]= is_winner(df_final["p2_i-2"].values[ind], df_final["p1_i-2"].values[ind])
    # #     df_final["winner_2"].values[ind]=  df_final["winner_1"].values[ind] + is_winner(df_final["p2_i-1"].values[ind], df_final["p1_i-1"].values[ind])
    # #     df_final["winner_3"].values[ind]=  df_final["winner_2"].values[ind] + is_winner(df_final["p2_i"].values[ind], df_final["p1_i"].values[ind])

    df_final = df_final.astype(int)



    return df_final

def create_results_table():
    return pd.DataFrame(0,index=[0],columns=["p1_i-1","p2_i-1","p1_i-2","p2_i-2"])

def update_results_table(player, computer, game_ind, table_ind, table):
    if (game_ind+1) %3==1:
        table = table.append(pd.Series([0,0,0,0],index=["p1_i-1","p2_i-1","p1_i-2","p2_i-2"], name=str(game_ind)))

        table["p1_i-2"].values[table_ind] = computer
        table["p2_i-2"].values[table_ind] = player
        # print(table)

    elif (game_ind+1) %3==2:
        table["p1_i-1"].values[table_ind]= computer
        table["p2_i-1"].values[table_ind] = player
        # print(table)


    return table


def number_to_action(num):
    actions = ["Rock","Paper","Scissors"]
    return actions[num-1]

def action_to_number(action):
    if action == "Rock":
        return 1
    elif action=="Paper":
        return 2
    elif action=="Scissors":
        return 3


data = pd.read_csv('data/Rock_Paper_Scissors_Raw.csv')

df = pd.DataFrame(data)
KNN_train(ML_DATA.final_organize(df))



