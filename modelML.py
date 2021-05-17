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


def prediction_NB(X_train, X_test, y_train):
    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)



def prediction_KNN(X_train, X_test, y_train):
    neigh = KNeighborsClassifier(n_neighbors=int(np.sqrt(X_train.shape[0])))
    neigh.fit(X_train, y_train)

    return neigh.predict(X_test)

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




def prediction_trees(X_train,X_test,y_train):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    return clf.predict(X_test)

# def prediction_LinearRegression(X_train,X_test, y_train):
#     reg = LinearRegression().fit(X_train, y_train)
#
#     print(reg.score(X_train, y_train))
#
#
#
#     return reg.predict(X_test)

def predict_():
    data = pd.read_csv("data/Rock_Paper_Scissors_Raw.csv")
    df = pd.DataFrame(data)

    df_final =ML_DATA.final_organize(df)
    df_final['winner_1'] = None
    df_final['winner_2'] = None
    df_final['winner_3'] = None

    for ind in df_final.index:
        df_final["winner_1"].values[ind]= is_winner(df_final["p2_i-2"].values[ind], df_final["p1_i-2"].values[ind])

        df_final["winner_2"].values[ind]=  df_final["winner_1"].values[ind] + is_winner(df_final["p2_i-1"].values[ind], df_final["p1_i-1"].values[ind])

        df_final["winner_3"].values[ind]=  df_final["winner_2"].values[ind] + is_winner(df_final["p2_i"].values[ind], df_final["p1_i"].values[ind])

    df_final = df_final.astype(int)

    # df_final["p2_1"] = is_win
    y = df_final["p2_i"]
    y = y.astype('int')
    print(y)
    X = df_final.drop(columns=["p2_i","p1_i","winner_3"])

    # X["p2_i-1"] = -1*X["p2_i-1"]
    # X["p2_i-2"] = -1*X["p2_i-2"]

    print(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.7, random_state = 0)


    #PREDICTIONS

    start_KNN = time.time()
    y_predicted_KNN = prediction_KNN(X_train, X_test, y_train)
    end_KNN = time.time()

    start_tree = time.time()
    y_predicted_tree = prediction_trees(X_train,X_test,y_train)

    end = time.time()

    # y_predicted_LinearReg = prediction_LinearRegression(X_train, X_test, y_train)

    y_pred_NB = prediction_NB(X_train,X_test, y_train )

    KNN_accuracy = accuracy_score(y_test, y_predicted_KNN)
    trees_accuracy = accuracy_score(y_test, y_predicted_tree)

    # lg_accuracy = (y_predicted_LinearReg == y_test).value_counts()

    # print(X_test.shape[0])

    print("KNN:",KNN_accuracy)
    print("tree:", trees_accuracy)

    print(y_predicted_tree, y_test.values)
    # print("lg_accuracy:", lg_accuracy)

    # rows_num = y_predicted_tree.shape[0]
    # s_trees = pd.Series(X_test["p1_i"].values)
    # s_test = pd.Series(y_test.values)

    # print("arrived  df_winners....")
    # # df_winners = pd.DataFrame(X_test["p1_i"].values,y_test.values,np.zeros(rows_num))
    # # print(df_winners)
    # for ind in range(rows_num):
    #     print(s_trees[ind], s_test[ind])
    #     if s_trees[ind] == 1 and s_test[ind]==3:
    #         print("winner")




predict_()


