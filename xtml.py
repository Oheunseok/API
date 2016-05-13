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


url=urllib.request.urlopen("http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101")
tree=ET.parse(url)
#tree=ET.parse("MovieList.xml")
note=tree.getroot()


List(tree)

indent(note)
#ET.dump(note)

print(note.findtext("boxofficeType"))
print(note.findtext("showRange"))
for element in note.findall("dailyBoxOfficeList"):
    for tag in element.findall("dailyBoxOffice"):
        print("rnum ",tag.findtext("rnum"))
        print("rank ",tag.findtext("rank"))
        print("rankInten",tag.findtext("rankInten"))
        print("rankOldAndNew",tag.findtext("rankOldAndNew"))
        print("movieCd", tag.findtext("movieCd"))
        print("movieNm", tag.findtext("movieNm"))
        print("openDt", tag.findtext("openDt"))
        print("salesAmt", tag.findtext("salesAmt"))
        print("salesShare", tag.findtext("salesShare"))
        print("salesInten", tag.findtext("salesInten"))
        print("salesChange", tag.findtext("salesChange"))
        print("salesAcc", tag.findtext("salesAcc"))
        print("audiCnt", tag.findtext("audiCntaudiCnt"))
        print("audiInten", tag.findtext("audiInten"))
        print("audiChange", tag.findtext("audiChange"))
        print("salesAcc", tag.findtext("salesAcc"))
        print("scrnCnt", tag.findtext("scrnCnt"))
        print("showCnt", tag.findtext("showCnt"))







        print()



#for parent in tree.getiterator():
#    for child in parent:
#        print(child)








#ET.ElementTree(note).write("MovieList.xml")
