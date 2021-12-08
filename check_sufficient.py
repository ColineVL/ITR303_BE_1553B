import numpy as np

from help import BANDWIDTH


def get_micro_period(messages_array):
    """
    Retourne la micro période de l'array des messages
    """
    # On se crée un tableau de fréquences
    frequencies = np.array(
        [float(message_dict["frequence"]) for message_dict in messages_array]
    )
    # On calcule le max des fréquences, et on en déduit la plus petite période
    return 1 / np.max(frequencies)


def check_sufficient_ord_cond(messages_array):
    """
    Vérification de la conditions suffisante
    """
    t_microcycle = get_micro_period(messages_array)
    print("Checking sufficient...")
    print("t_microcycle (en secondes) = ", t_microcycle)
    c_sum = (
        np.sum([message_dict["sizeBits"] for message_dict in messages_array])
        / BANDWIDTH
    )
    print("c_sum = ", c_sum)
    print("test (c/microcycle) = ", c_sum / t_microcycle)
    return c_sum / t_microcycle <= 1
