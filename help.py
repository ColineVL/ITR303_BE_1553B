def temps2usecondes(arrayMessages):
    for message in arrayMessages:
        # délai de transmission (<DT>)
        message["DT"] = str(message["transDelay"] * 1e6)
        # délai d’accès au médium (<DMAC>)
        # délai de bout en bout(<DBEB>)
        # test d’ordonnançabilité(<Test>)
