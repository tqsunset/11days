from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.playdb.co.kr/playdb/playdblist.asp?sReqMainCategory=000001&sReqSubCategory=&sReqDistrict=&sReqTab=2&sPlayType=2&sStartYear=&sSelectType=2', headers=headers)

page = BeautifulSoup(data.text, 'html.parser')

# print(page)
trs = page.select('#contents > div.container1 > table > tr')
movieTable =trs[10]
extract = movieTable.select('td > table > tr > td > table > tr > td > table > tr > td > table')

for table in extract:
    playName = table.select_one('tr > td > b > font > a')
    if playName is not None:                #
        info = table.text.strip()
        infoParse = info.split(':')
        print(len(infoParse))

        infoParse[0] = infoParse[0].rstrip('세부장르 \n\t\r')
        infoParse[1] = infoParse[1].strip('일시 ')
        infoParse[2] = infoParse[2].strip('장소 ')
        infoParse[3] = infoParse[3].strip('출연 ')

        if len(infoParse) > 4:
                infoParse[4] = infoParse[4].strip('Staff ')
        elif len(infoParse) > 5:
            infoParse[5] = infoParse[5].strip()

        print(infoParse)    # rssplit는 시간이 걸린다
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
