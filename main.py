from parseXML import exportXML, parseXML
from computeD3 import calc_trans_delay_with_array
from help import calc_msg_size_bits_with_array
from check_sufficient import check_sufficient_ord_cond
from computeD2 import calc_access_delay_vect

# Etape 1 parse le XML
arrayMessages = parseXML("xmlB1-periodique.xml")

# On calcule les tailles des messages en bits
calc_msg_size_bits_with_array(arrayMessages)

# Etape 2 compute d3 delai de transmission
calc_trans_delay_with_array(arrayMessages)

# Etape 3 vérification de la condition nécessaire d’ordonnançabilité des messages
condition = check_sufficient_ord_cond(arrayMessages)
if condition:
    print("SC verified")
else:
    print("SC not verified!")

# Etape 4 calcul d2
calc_access_delay_vect(arrayMessages)

# Etape 5 export XML
exportXML(arrayMessages, "sortie.xml", condition)
