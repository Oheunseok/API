import xml.etree.ElementTree as ET
import urllib.request

#지금은 안씀
import ctypes
import gc

#일단 안씀
def List(tree):
    for parent in tree.getiterator():
        for child in parent:
            yield parent, child
#일자로 구성된 xml을 정리해줌
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
#일단 안씀
def objects_by_id(id_):
    for obj in gc.get_objects():
        if id(obj) == id_:
            return obj
    raise Exception("No found")

searchMovieList="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?"
key="key=430156241533f1d058c603178cc3ca0e"

year="2016"
mon="05"
date="13"
Dt="&targetDt="+year+mon+date
Nation="&repnationCd="+"F"

url=urllib.request.urlopen(searchMovieList+key+Dt+Nation)
tree=ET.parse(url)
#tree=ET.parse("MovieList.xml")
note=tree.getroot()

#정리해서 보여줌
indent(note)
#xml 문서 그대로 보여줌
#ET.dump(note)


print(note.findtext("boxofficeType"))
print(note.findtext("showRange"))
for element in note.findall("dailyBoxOfficeList"):
    for tag in element.findall("dailyBoxOffice"):
        print("순번\t\t\t\t\t",tag.findtext("rnum"))
        print("일일 박스오피스 순위\t",tag.findtext("rank"))
        print("전일대비 순위증감\t\t",tag.findtext("rankInten"))
        print("랭킹신규진입\t\t\t",tag.findtext("rankOldAndNew"))
        print("영화대표코드\t\t\t", tag.findtext("movieCd"))
        print("영화제목\t\t\t\t", tag.findtext("movieNm"))
        print("개봉일\t\t\t\t\t", tag.findtext("openDt"))
        print("매출액\t\t\t\t\t", tag.findtext("salesAmt"))
        print("매출지분율\t\t\t\t", tag.findtext("salesShare"))
        print("매출액 증감분\t\t\t", tag.findtext("salesInten"))
        print("매출액 증감률\t\t\t", tag.findtext("salesChange"))
        print("누적매출액\t\t\t\t", tag.findtext("salesAcc"))
        print("관람객수\t\t\t\t", tag.findtext("audiCnt"))
        print("관람객 증감분\t\t\t", tag.findtext("audiInten"))
        print("관람객 증감비율\t\t\t", tag.findtext("audiChange"))
        print("누적관객\t\t\t\t", tag.findtext("audiAcc"))
        print("상영스크린수\t\t\t", tag.findtext("scrnCnt"))
        print("상영횟수\t\t\t\t", tag.findtext("showCnt"))
        #공백용
        print()



#for parent in tree.getiterator():
#    for child in parent:
#        print(child)


#ET.ElementTree(note).write("MovieList.xml")
