import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

def prediction_KNN(X_train, X_test, y_train):
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X_train, y_train)

    return neigh.predict(X_test)


def prediction_trees(X_train,X_test,y_train):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    return clf.predict(X_test)

#
# def prediction_LinearRegression(X_train,X_test, y_train):
#     reg = LinearRegression().fit(X_train, y_train)
#
#     print(reg.score(X_train, y_train))
#
#
#
#     return reg.predict(X_test)

def main():
    data = pd.read_csv("data/RPS_tmp.csv")
    df = pd.DataFrame(data)

    X_train, X_test, y_train, y_test = train_test_split(df, df["p2_i"], test_size = 0.33, random_state = 42)


    #PREDICTIONS
    y_predicted_KNN = prediction_KNN(X_train, X_test, y_train)
    y_predicted_tree = prediction_trees(X_train,X_test,y_train)
    # y_predicted_LinearReg = prediction_LinearRegression(X_train, X_test, y_train)



    KNN_accuracy = accuracy_score(y_test, y_predicted_KNN)
    trees_accuracy = accuracy_score(y_test, y_predicted_tree)
    # lg_accuracy = LinearRegression.score(y_test,y_predicted_LinearReg)

    #
    # print("KNN:",KNN_accuracy)
    # print("tree:", trees_accuracy)


    # print("lg_accuracy:", lg_accuracy)

    rows_num = y_predicted_tree.shape[0]
    s_trees = pd.Series(X_test["p1_i"].values)
    s_test = pd.Series(y_test.values)

    print("arrived  df_winners....")
    # df_winners = pd.DataFrame(X_test["p1_i"].values,y_test.values,np.zeros(rows_num))
    # print(df_winners)
    for ind in range(rows_num):
        print(s_trees[ind], s_test[ind])
        if s_trees[ind] == 1 and s_test[ind]==3:
            print("winner")









main()