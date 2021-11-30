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
