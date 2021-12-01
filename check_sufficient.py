import numpy as np
from help import calc_msg_size_bits

MASTER = "SXJJ"
BANDWIDTH = 1e6


def get_micro_period(messages_array):
    frequencies = np.array(
        [float(message_dict["frequence"]) for message_dict in messages_array]
    )
    return 1 / np.max(frequencies)


def check_sufficient_ord_cond(messages_array):
    l_arrays = np.array(
        [calc_msg_size_bits(message_dict) for message_dict in messages_array]
    )
    t_microcycle = get_micro_period(messages_array)
    c_sum = np.sum(l_arrays) / BANDWIDTH
    return c_sum / t_microcycle <= 1
