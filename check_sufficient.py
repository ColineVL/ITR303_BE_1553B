import numpy as np

MASTER = "SXJJ"
BANDWIDTH = 1e6


def get_micro_period(messages_array):
    frequencies = np.array(
        [float(message_dict["frequence"]) for message_dict in messages_array]
    )
    return 1 / np.max(frequencies)


def check_sufficient_ord_cond(messages_array):
    t_microcycle = get_micro_period(messages_array)
    print("t_microcycle = ", t_microcycle)
    c_sum = (
        np.sum([message_dict["sizeBits"] for message_dict in messages_array])
        / BANDWIDTH
    )
    print("c_sum = ", c_sum)
    print("test = ", c_sum / t_microcycle)
    #print(c_sum / t_microcycle)
    return c_sum / t_microcycle <= 1
