MASTER = "SXJJ"
BANDWIDTH = 1e6


def calc_trans_delay(message_dict):
    return message_dict["sizeBits"] / BANDWIDTH


def calc_trans_delay_with_array(messages_array):
    for message in messages_array:
        message["transDelay"] = calc_trans_delay(message)
