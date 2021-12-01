import numpy as np
from numpy.lib.index_tricks import c_

MASTER = "SXJJ"
BANDWIDTH = 1e6


def calc_msg_size_bits(message_dict):
    """
    message_dict["taille_mes"] est en nombre de mots
    un mot fait 20 bits (empaquete)
    """
    overhead_com = (
        56
        if (message_dict["emetteur"] == MASTER or message_dict["recepteur"] == MASTER)
        else 106
    )
    taille_tot = overhead_com + 20 * int(message_dict["taille_mes"])
    return taille_tot


def calc_trans_delay(message_dict):
    return calc_msg_size_bits(message_dict) / BANDWIDTH


def calc_trans_delay_with_array(messages_array):
    for message in messages_array:
        message["transDelay"] = calc_trans_delay(message)


def get_micro_period(messages_array):
    frequencies = np.array([
        float(message_dict["frequence"]) for message_dict in messages_array
    ])
    return 1/np.max(frequencies)


def check_sufficient_ord_cond(messages_array):
    l_arrays = np.array([
        calc_msg_size_bits(message_dict) for message_dict in messages_array
    ])
    t_microcycle = get_micro_period(messages_array)
    c_sum = np.sum(l_arrays)/BANDWIDTH
    return c_sum/t_microcycle <= 1

