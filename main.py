import xml.etree.ElementTree as ET
import urllib.request
import Func
from Func import indent


key="key=430156241533f1d058c603178cc3ca0e"


year="2016"
mon="05"
date="13"
Dt="&targetDt="+year+mon+date
Nation="&repnationCd="+"F"

Operation=input("오퍼레이션 선택:")
if(Operation=="일일"):
    Oper="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?"     #일일
    url = urllib.request.urlopen(Oper + key + Dt + Nation)
elif(Operation=="주간"):
    Oper="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.xml?"    #주간
    url = urllib.request.urlopen(Oper + key + Dt + Nation)
elif(Operation=="목록"):
    Oper="http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml?"  #목록
    url = urllib.request.urlopen(Oper + key)


# year="2016"
# mon="05"
# date="13"
# Dt="&targetDt="+year+mon+date
# Nation="&repnationCd="+"F"

# url=urllib.request.urlopen(Oper+key+Dt+Nation)

tree = ET.parse(url)
note=tree.getroot()


#정리해서 보여줌
indent(note)

#xml 문서 그대로 보여줌
#ET.dump(note)

if Operation=="일일":
    Func.daily(note)
elif Operation=="주간":
    Func.weekly(note)
elif Operation=="목록":
    Func.MovieList(note)

# def MoveList():
#     for element in note.findall("weeklyBoxOfficeList"):
#         for tag in element.findall("weeklyBoxOffice"):
#             print("영화대표코드\t\t\t\t\t", tag.findtext("movieCd"))
#             print("영화명(국)\t\t\t", tag.findtext("movieNm"))
#             print("영화명(외)\t\t", tag.findtext("movieNmEn"))
#             print("제작연도\t\t\t", tag.findtext("prdtYear"))
#             print("개봉연도\t\t\t", tag.findtext("openDt"))
#             print("영화유형\t\t\t\t", tag.findtext("typeNm"))
#             print("제작상태\t\t\t\t\t", tag.findtext("prdtStatNm"))
#             print("제작국가\t\t\t\t\t", tag.findtext("nationAlt"))
#             print("영화장르\t\t\t\t", tag.findtext("genreAlt"))
#             print("대표 제작국가명\t\t\t", tag.findtext("repNationNm"))
#             print("대표 장르명\t\t\t", tag.findtext("repGenreNm"))
#
#             # print("상영스크린수\t\t\t", tag.findtext("peopleNm"))
#
#             # print("상영횟수\t\t\t\t", tag.findtext("companyCd"))
#             # print("상영횟수\t\t\t\t", tag.findtext("companyNm"))
#             # 공백용
#             print()




#ET.ElementTree(note).write("MovieList.xml")

