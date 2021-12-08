import numpy as np
import pandas as pd
import math as mt

from help import BANDWIDTH


def calc_access_delay_vect(message_dict_array):
    """
    for every message calculates the media access delay
    d2 = WCRT - d3

    assigning priority to tasks according to RM
    priority in ascending order
    => priority = frequence
    """

    # transform input to dataframe for ease of manipulation
    messages_df = pd.DataFrame(message_dict_array)
    messages_df = messages_df.astype(
        dtype={
            "frequence": float,
            "taille_mes": int,
            "sizeBits": int,
            "DT": float,
        }
    )
    messages_df["C"] = messages_df["sizeBits"] / BANDWIDTH

    wcrt_dict = {}
    for index in messages_df.index:

        # Split messages by strictly lower and upper priorities
        strictly_less_prior_msgs_df = messages_df[
            messages_df["frequence"] < messages_df.loc[index]["frequence"]
        ]
        more_prior_msg_df = messages_df[
            messages_df["frequence"] >= messages_df.loc[index]["frequence"]
        ]
        more_prior_msg_df = more_prior_msg_df.drop(index=index)

        # calculate WCRT for every message iteratively
        # Ci = msg_length
        # Wi+1 = Ci + max(Cj, less prior) + sum(Cj*[Wi/Tj], more prior)
        W = messages_df.loc[index]["C"]
        T = 1 / messages_df.loc[index]["frequence"]
        W_old = 0
        while W != W_old:
            W_old = W
            c1 = messages_df.loc[index]["C"]
            intermediaire = strictly_less_prior_msgs_df["C"].max()
            less_prior_max = intermediaire if not np.isnan(intermediaire) else 0
            more_prior_sum = (
                more_prior_msg_df["C"]
                * more_prior_msg_df["frequence"].apply(lambda x: mt.ceil(W * x))
            ).sum()
            W = c1 + less_prior_max + more_prior_sum
            if W > T:
                print("W>T reached")
                print(message_dict_array[index])
                print(T)
                print(W)
                print(W_old)
                W = np.nan
                break
        wcrt_dict[index] = W
    messages_df["DBEB"] = pd.Series(wcrt_dict)

    # b2 = DBEB - b3
    messages_df["DMAC"] = messages_df["DBEB"] - messages_df["DT"]

    # add results to the array of messages
    for index in messages_df.index:
        message_dict_array[index]["DMAC"] = messages_df.loc[index]["DMAC"]
        message_dict_array[index]["DBEB"] = messages_df.loc[index]["DBEB"]
    
    return
