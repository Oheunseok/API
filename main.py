import xml.etree.ElementTree as ET
import urllib.request
import Func
import datetime,time
from Func import indent


key="key=9a3bdfabc4837b2691c9b0f17c7d2575"
t=datetime.date.today()

# Today=str(t).replace("-","")
yesterday = datetime.date.today() + datetime.timedelta(days=-1)
Yesterday=str(yesterday).replace("-","")


year="2016"
mon="05"
date="22"

print("어제날짜: "+Yesterday)    #오늘껀 통계가 안나와서 출력이 안됨
Dt="&targetDt="+year+mon+date
# Dt="&targetDt="+Yesterday
Nation="&repnationCd="+"F"

while(1):
    Operation=input("오퍼레이션 선택:")
    if(Operation == "일일"): #일일은 전날까지만
        Oper = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?"     #일일
        url = urllib.request.urlopen(Oper + key + Dt + Nation)
    elif(Operation == "주간"): #주간은 입력한 날짜에 해당하는 주의 주말(금~일요일까지 집계한 내용을 보여줌)
        Oper = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.xml?"    #주간
        url = urllib.request.urlopen(Oper + key + Dt + Nation)
    elif(Operation == "영화목록"):
        Oper = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml?"  #목록
        url = urllib.request.urlopen(Oper + key)
    elif(Operation == "영화사목록"):
        Oper = "http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.xml?"  # 목록
        url = urllib.request.urlopen(Oper + key)

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
    elif Operation=="영화목록":
        Func.MovieList(note)
    elif Operation=="영화사목록":
        Func.CompanyList(note)



    ET.ElementTree(note).write("XML_test.xml")

