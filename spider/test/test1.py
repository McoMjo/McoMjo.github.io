import re
import bs4
import urllib.request,urllib.error
import xlwt
import requests
import sqlite3
from bs4 import BeautifulSoup

#爬！！！
def getdate(baseurl):
    datalist = []
    i = 1
    # for i in range(1, 101):
    url = baseurl + str(i)
    html = askURl(url)
    # 解析
    soup  = BeautifulSoup(html, "html.parser")
    position                = soup.find_all('a',class_="reco-job-title")
    print(position[0].string)
    print(position)
    company                 = soup.find_all('div', class_="reco-job-com")
    location                = soup.find_all('span', class_="nk-txt-ellipsis js-nc-title-tips job-address")
    print(location[0].text)
    print(location)
    # for j in range(0, len(location)):
    #     print(location[j].string)
    #     print(len(location))
    salary                  = soup.find_all('div', class_="reco-job-info")
    print(salary[0].div.contents[3].contents[0].next_sibling)
    print(len(salary))
    release_time            = soup.find_all('span', string=re.compile('前'))
    print(release_time[0].string)
    print(release_time)
    processing_rate         = soup.find_all('span', class_="intern_center js-nc-title-tips")
    print(processing_rate[0].string)
    print(processing_rate)
    # print(len(position))
    # print(len(company))
    # print(len(location))
    # print(len(salary))
    # print(len(release_time))
    # print(len(processing_rate))


    for j in range(0, len(position)):
        datalist.append(
            {
                'position': position[j].string,
                'company': company[j].a.string,
                #'location': location[j].string,
                'salary': salary[j].div.contents[3].contents[0].next_sibling,
                'release_time': release_time[j].string,
               # 'processing_rate': processing_rate[j].string
            }
        )

def askURl(url):
    cookie = 'NOWCODERUID=18EF7842F941476219BE8C096512B1DC; NOWCODERCLINETID=DB66796ACDB79C031F7BDB8D0767A482; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1603198410,1603206409; t=17FD8F801C07074D01059C7FF3DD0695; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1603244754; SERVERID=20209ceebe066108970cd5046744d133|1603256551|1603244144'
    head = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 78.0.3904.108 Safari / 537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Cookie': cookie
}
    seesion = requests.session()
    request = seesion.get(url, headers=head)
    html = request.text
    return html

if __name__=="__main__":
    path = r"D:\pythonProject2\spider\niukewang.xlsx"
    url = "https://www.nowcoder.com/intern/center?recruitType=1&page="
    datalist = getdate(url)
