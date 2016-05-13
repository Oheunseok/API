import xml.etree.ElementTree as ET
import ctypes
import urllib.request
import gc


def List(tree):
    for parent in tree.getiterator():
        for child in parent:
            yield parent, child

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def objects_by_id(id_):
    for obj in gc.get_objects():
        if id(obj) == id_:
            return obj
    raise Exception("No found")

tree=ET.parse("MovieList.xml")
note=tree.getroot()

print (note.findtext("boxofficeType"))
List(tree)

indent(note)
ET.dump(note)


for parent in tree.getiterator():
    for child in parent:
        print(child)








#ET.ElementTree(note).write("MovieList.xml")
