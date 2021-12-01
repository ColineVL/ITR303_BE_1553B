from help import calc_msg_size_bits

MASTER = "SXJJ"
BANDWIDTH = 1e6


def calc_trans_delay(message_dict):
    return calc_msg_size_bits(message_dict) / BANDWIDTH


def calc_trans_delay_with_array(messages_array):
    for message in messages_array:
        message["transDelay"] = calc_trans_delay(message)
