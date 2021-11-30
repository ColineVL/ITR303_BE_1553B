from parseXML import exportXML, parseXML
from computeD3 import calc_trans_delay_with_array
from help import temps2usecondes

# Etape 1 parse le XML
arrayMessages = parseXML("xmlB1-periodique.xml")
# print(array[0]["nom"])

# Etape 2 compute d3 delai de transmission
calc_trans_delay_with_array(arrayMessages)

# Etape 5 export XML
temps2usecondes(arrayMessages)
exportXML(arrayMessages, "sortie.xml")
