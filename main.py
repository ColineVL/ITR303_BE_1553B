from parseXML import exportXML, parseXML
from computeD3 import calc_trans_delay_with_array
from help import temps2usecondes
from check_sufficient import check_sufficient_ord_cond

# Etape 1 parse le XML
arrayMessages = parseXML("xmlB1-periodique.xml")
# print(array[0]["nom"])

# Etape 2 compute d3 delai de transmission
calc_trans_delay_with_array(arrayMessages)

# Etape 3 vérification de la condition nécessaire d’ordonnançabilité des messages
check = check_sufficient_ord_cond(arrayMessages)
print(check)

# Etape 5 export XML
temps2usecondes(arrayMessages)
exportXML(arrayMessages, "sortie.xml")
