import re
import bs4
import urllib.request,urllib.error
import xlwt
import requests
import sqlite3
from bs4 import BeautifulSoup

#爬！！！
def getdate(page, baseurl,path):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('niukewang', cell_overwrite_ok=True)
    col = ("position", "company", "location", "release_time", "processing_rate", 'salary')
    data_position_list = []
    data_company_list = []
    data_location_list = []
    data_salary_list = []
    data_processing_rate_list = []
    data_release_time_list = []
    for i in range(0, 6):#打印头部
        sheet.write(0, i, col[i])
    for i in range(1, int(page)):
        idex = i-1
        url = baseurl + str(i)
        html = askURl(url)
        # 解析
        soup = BeautifulSoup(html, "html.parser")
        position = soup.find_all('a', class_="reco-job-title")
        company = soup.find_all('div', class_="reco-job-com")
        location = soup.find_all('span', class_="nk-txt-ellipsis js-nc-title-tips job-address")
        salary                  = soup.find_all('div', class_="reco-job-info")
        release_time = soup.find_all('span', string=re.compile('前'))
        processing_rate = soup.find_all('span', class_="intern_center js-nc-title-tips")
        for j in range(0, len(position)):
            data_position_list.append(position[j].string)

        for j in range(0, len(company)):
            data_company_list.append(company[j].a.string)

        for j in range(0, len(location)):
            data_location_list.append(location[j].text)

        for j in range(0, len(salary)):
            data_salary_list.append(salary[j].div.contents[3].contents[0].next_sibling)

        for j in range(0, len(release_time)):
            data_release_time_list.append(release_time[j].string)

        for j in range(0, len(processing_rate)):
            data_processing_rate_list.append(processing_rate[j].string)

        for j in range(0, len(data_position_list)):
            sheet.write(j + 1 + idex * 30, 0, data_position_list[j])

        for j in range(0, len(data_company_list)):
            sheet.write(j + 1 + idex * 30, 1, data_company_list[j])

        for j in range(0, len(data_location_list)):
            sheet.write(j + 1 + idex * 30, 2, data_location_list[j])

        for j in range(0, len(data_salary_list)):
             sheet.write(j + 1 + idex * 30, 5, data_salary_list[j])

        for j in range(0, len(data_release_time_list)):
            sheet.write(j + 1 + idex * 30, 3, data_release_time_list[j])

        for j in range(0, len(data_processing_rate_list)):
            sheet.write(j + 1 + idex * 30, 4, data_processing_rate_list[j])

            book.save(path)

#获得url
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
    path = r"D:\pythonProject2\spider\niukewang.xls"
    url = "https://www.nowcoder.com/intern/center?recruitType=1&page="
    page = input("你想看前几页?")
    getdate(page, url, path)
    print('爬完了！！')

