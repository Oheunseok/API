import xml.etree.ElementTree as ET

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



def daily(note):
    print(note.findtext("boxofficeType"))
    print(note.findtext("showRange"))
    for element in note.findall("dailyBoxOfficeList"):
        for tag in element.findall("dailyBoxOffice"):
            print("순번\t\t\t\t\t", tag.findtext("rnum"))
            print("일일 박스오피스 순위\t", tag.findtext("rank"))
            print("전일대비 순위증감\t\t", tag.findtext("rankInten"))
            print("랭킹신규진입\t\t\t", tag.findtext("rankOldAndNew"))
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
            # 공백용
            print()

def weekly(note):
    print(note.findtext("boxofficeType"))
    print(note.findtext("showRange"))
    for element in note.findall("weeklyBoxOfficeList"):
        for tag in element.findall("weeklyBoxOffice"):
            print("순번\t\t\t\t\t",tag.findtext("rnum"))
            print("주간/주말 순위\t\t\t",tag.findtext("rank"))
            print("전주대비 순위증감\t\t",tag.findtext("rankInten"))
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

def MovieList(note):
    for element in note.findall("movieList"):
        for tag in element.findall("movie"):
            print("영화대표코드\t\t", tag.findtext("movieCd"))
            print("영화명(국)\t\t\t", tag.findtext("movieNm"))
            print("영화명(외)\t\t\t", tag.findtext("movieNmEn"))
            print("제작연도\t\t\t", tag.findtext("prdtYear"))
            print("개봉연도\t\t\t", tag.findtext("openDt"))
            print("영화유형\t\t\t", tag.findtext("typeNm"))
            print("제작상태\t\t\t", tag.findtext("prdtStatNm"))
            print("제작국가\t\t\t", tag.findtext("nationAlt"))
            print("영화장르\t\t\t", tag.findtext("genreAlt"))
            print("대표 제작국가명\t\t", tag.findtext("repNationNm"))
            print("대표 장르명\t\t\t", tag.findtext("repGenreNm"))

            # print("상영스크린수\t\t\t", tag.findtext("peopleNm"))

            # print("상영횟수\t\t\t\t", tag.findtext("companyCd"))
            # print("상영횟수\t\t\t\t", tag.findtext("companyNm"))
            # 공백용
            print()

#def MovieInfo(note):
    #for element in note.findall("movieInfoResult"):
        #for tag in element.findall("movieInfo"):
            # #print("영화대표코드\t\t", tag.findtext("movieCd"))
           # print("영화명(국)\t\t\t", tag.findtext("movieNm"))
           # print("영화명(외)\t\t\t", tag.findtext("movieNmEn"))
            #print("영화명(원문)\t\t\t", tag.findtext("movieNmOg"))
            #print("제작연도\t\t\t", tag.findtext("prdtYear"))
            #print("상영시간\t\t\t", tag.findtext("showTm"))
            #print("개봉연도\t\t\t", tag.findtext("openDt"))
            #print("영화유형\t\t\t", tag.findtext("typeNm"))
           # print("제작상태\t\t\t", tag.findtext("prdtStatNm"))
            #print("제작국가\t\t\t", tag.findtext("nations"))
            #print("제작국가명\t\t", tag.findtext("nationNm"))
            #print("장르명\t\t\t", tag.findtext("genreNm"))
            #print("감독\t\t\t", tag.findtext("directors"))
            #print("감독명\t\t\t", tag.findtext("peopleNm"))
            #print("제작연도\t\t\t", tag.findtext("peopleNmEn"))
            #print("상영시간\t\t\t", tag.findtext("actors"))
            #print("개봉연도\t\t\t", tag.findtext("peopleNm"))
            #print("영화유형\t\t\t", tag.findtext("peopleNmEn"))
            #print("제작상태\t\t\t", tag.findtext("cast"))
            #print("제작국가\t\t\t", tag.findtext("castEn"))
            #print("영화장르\t\t\t", tag.findtext("showTypes"))
            #print("상영형태 구분\t\t", tag.findtext("showTypeGroupNm"))
            #print("상영형태명\t\t\t", tag.findtext("showTypeNm"))
            #print("심의정보\t\t", tag.findtext("audits"))
            #print("심의번호\t\t\t", tag.findtext("auditNo"))
            #print("관람등급 명칭\t\t\t", tag.findtext("watchGradeNm"))
    #for element in note.findall("companys"):
        #for tag in element.findall("company"):
            #print("참여 영화사 코드\t\t\t", tag.findtext("companyCd"))
            #print("참여 영화사명\t\t\t", tag.findtext("companyNm"))
            #print("참여 영화사명(영문)\t\t\t", tag.findtext("companyNmEn"))
            #print("참여 영화사 분야명\t\t\t", tag.findtext("companyPartNm"))
            #print("스텝\t\t\t", tag.findtext("staffs"))
            #print("스텝명\t\t\t", tag.findtext("peopleNm"))
            #print("스텝명(영문)\t\t\t", tag.findtext("peopleNmEn"))
            #print("스텝역할명\t\t", tag.findtext("staffRoleNm"))


            # print("상영스크린수\t\t\t", tag.findtext("peopleNm"))

            # print("상영횟수\t\t\t\t", tag.findtext("companyCd"))
            # print("상영횟수\t\t\t\t", tag.findtext("companyNm"))
            # 공백용
            print()

def MovieCopList(note):
    print(note.findtext("companyListResult"))
    print(note.findtext("totCnt"))
    for element in note.findall("companyList"):
        for tag in element.findall("company"):
            print("영화사대표코드\t\t", tag.findtext("companyCd"))
            print("영화사명(국)\t\t\t", tag.findtext("companyNm"))
            print("영화사명(외)\t\t\t", tag.findtext("companyNmEn"))
            print("영화사 분류\t\t\t", tag.findtext("companyPartNames"))
            print("대표자명\t\t\t", tag.findtext("ceoNm"))
            print("필모리스트\t\t\t", tag.findtext("filmoNames"))
            # print("상영스크린수\t\t\t", tag.findtext("peopleNm"))

            # print("상영횟수\t\t\t\t", tag.findtext("companyCd"))
            # print("상영횟수\t\t\t\t", tag.findtext("companyNm"))
            # 공백용
            print()