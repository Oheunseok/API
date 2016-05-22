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
elif(Operation=="영화사목록"):
    Oper="http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.xml?"  #영화사목록
    url = urllib.request.urlopen(Oper + key)
#elif(Operation=="영화정보"):
   # Oper="http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml?"  #영화정보
    #url = urllib.request.urlopen(Oper + key + Dt + Nation)


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
elif Operation=="영화사목록":
    Func.MovieCopList(note)
#elif Operation=="영화정보":
   # Func.MovieInfo(note)


#ET.ElementTree(note).write("MovieList.xml")

