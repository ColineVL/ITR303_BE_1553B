MASTER = "SXJJ"
BANDWIDTH = 1e6


def temps2usecondes(arrayMessages):
    for message in arrayMessages:
        # délai de transmission (<DT>)
        message["DT"] = str(message["transDelay"] * 1e6)
        # délai d’accès au médium (<DMAC>)
        # délai de bout en bout(<DBEB>)
        # test d’ordonnançabilité(<Test>)


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
