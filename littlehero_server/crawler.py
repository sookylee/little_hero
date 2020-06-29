import requests
from bs4 import BeautifulSoup
import json
import os

URL = 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do'
SHOW = '?type=show&progrmRegistNo='
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get(URL)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
temp = soup.select('#content > div.content_view > div.board_list.board_list2.non_sub > ul > li > input')


for li in temp :
    val = li.attrs['value']
    print(val)
    for no in val :
        res = requests.get(URL+SHOW+no)
        res_html = res.text
        res_soup = BeautifulSoup(html, 'html.parser')
        tmp = res_soup.select('#content > div.content_view > div > div.board_view.type2 > h3')
        title = tmp.select('input').attrs['value']
        tmpStatus = tmp.select('em').string
        if tmpStatus == '(모집중)' :
            recruit_status = True
        else :
            recruit_status = False
        do_date = res_soup.select('#content > div.content_view > div > div.board_view.type2 > div.board_data.type2 > div:nth-child(1) > dl:nth-child(1) > dd').string
        do_time = res_soup.select('#content > div.content_view > div > div.board_view.type2 > div.board_data.type2 > div:nth-child(1) > dl:nth-child(2) > dd').string
        recruit_date = res_soup.select('#content > div.content_view > div > div.board_view.type2 > div.board_data.type2 > div:nth-child(2) > dl:nth-child(1) > dd').string
        do_week = res_soup.select('#content > div.content_view > div > div.board_view.type2 > div.board_data.type2 > div:nth-child(2) > dl:nth-child(2) > dd').string
        recruit_member = res_soup.select('#content > div.content_view > div > div.board_view.type2 > div.board_data.type2 > div:nth-child(3) > dl:nth-child(1) > dd').string
        domain = res_soup.select('#content > div.content_view > div > div.board_view.type2 > div.board_data.type2 > div:nth-child(4) > dl:nth-child(1) > dd').string
        

