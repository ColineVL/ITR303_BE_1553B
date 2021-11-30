# Import required library
import xml.etree.cElementTree as ET
import xml.etree.ElementTree as xml


def parseXML(file_name):
    array = []
    # Parse XML with ElementTree
    tree = ET.ElementTree(file=file_name)
    print(tree.getroot())
    root = tree.getroot()
    print("tag=%s, attrib=%s" % (root.tag, root.attrib))

    # get the information via the children!
    messages = root.getchildren()
    for message in messages:
        prop = message.getchildren()
        m = {}
        for prop in message:
            # print("%s=%s" % (prop.tag, prop.text))
            m[prop.tag] = prop.text
        array.append(m)
    return array


def exportXML(array, filename):
    # Start with the root element
    root = xml.Element("fichier")
    root.attrib["titre"] = "BUS 1553B B1  "

    for message in array:
        child1 = xml.Element("message")
        root.append(child1)

        keys = [
            "nom",
            "type",
            "frequence",
            "taille_mes",
            "emetteur",
            "recepteur",
            "DT",
            # "DMAC",
            # "DBEB",
            # "Test",
        ]
        for key in keys:
            msgNode = xml.SubElement(child1, key)
            msgNode.text = message[key]

    tree = xml.ElementTree(root)
    with open(filename, "wb") as fh:
        tree.write(fh)
