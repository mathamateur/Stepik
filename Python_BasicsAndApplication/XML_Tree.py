from xml.etree import ElementTree

RGB ={"red":0,"green":0,"blue":0}


def counter(root,d):
    RGB[root.attrib["color"]] += d
    for child in root:
        counter(child,d+1)


root = ElementTree.fromstring(input())
counter(root,1)
print(str(RGB["red"])+" "+str(RGB["green"])+" "+str(RGB["blue"]))