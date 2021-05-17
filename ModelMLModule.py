import pandas as pd
from pandasgui import show
import numpy as np

NUM_OF_IDS =148543


def rem_less_than_3(df):
    tmp = df["game_id"].value_counts()
    c = tmp.where(tmp < 3)
    c_int = pd.Series(c.dropna(), dtype="int")

    indexes = df['game_id'].isin(c_int.index)
    tmp1 = indexes.where(indexes).dropna().index.values
    df = df.drop(index=tmp1)

    # The new modified dataframe
    return df.reset_index().drop(columns="index")

def rem_useless_values(df):
    tmp = df["game_id"].value_counts()
    c = tmp.where(tmp > 3)
    c_int = pd.Series(c.dropna(), dtype="int")

    return df.groupby('game_id').head(3).reset_index().drop(columns="index")

def final_organize(df_new):
    df_new = rem_useless_values(rem_less_than_3(df))

    df_new = pd.concat(
        [
            df_new,
            pd.DataFrame(
                [[np.nan, np.nan, np.nan, np.nan]],
                index=df_new.index,
                columns=["p1_i-1", "p2_i-1", "p1_i-2", "p2_i-2"]
            )
        ], axis=1
    )

    last_1 = -1
    last_2 = -1
    for ind in range(3, df_new.shape[0], 3):
        df_new.at[ind, "p1_i-1"] = df_new.at[ind - 1, "p1_i"]
        df_new.at[ind, "p2_i-1"] = df_new.at[ind - 1, "p2_i"]

        df_new.at[ind, "p1_i-2"] = df_new.at[ind - 2, "p1_i"]
        df_new.at[ind, "p2_i-2"] = df_new.at[ind - 2, "p2_i"]

        df_new.at[ind - 1, "p1_i"] = None
        df_new.at[ind - 1, "p2_i"] = None
        df_new.at[ind - 2, "p1_i"] = None
        df_new.at[ind - 2, "p2_i"] = None

    df_new = df_new.drop(columns=["game_id", "game_round_id"])

    df_final = df_new.dropna().astype(int).reset_index().drop(columns=["index"])

    return df_final


#import
data = pd.read_csv("data/Rock_Paper_Scissors_Raw.csv")
df = pd.DataFrame(data)
# df_new = pd.DataFrame(index=np.arange(148543), columns=["p1_i","p2_i","p1_i-1",'p2_i-1',"p1_i-2","p2_i-2"])




