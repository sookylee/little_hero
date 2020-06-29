import requests
from bs4 import BeautifulSoup
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "littlehero_server.settings")
import django
django.setup()

from announcement.models import Post

def parser_1365() :
    URL = 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do'
    SHOW = '?type=show&progrmRegistNo='

    req = requests.get(URL)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.select('#content > div.content_view > div.board_list.board_list2.non_sub > ul > li > input')

    result = []
    for li in temp :
        data = {}
        val = li.attrs['value']
        data['regist_no'] = int(val)
        res = requests.get(URL+SHOW+val)
        res_html = res.text
        res_soup = BeautifulSoup(res_html, 'html.parser')
        tmp = res_soup.select('#content > div.content_view > div > div.board_view.type2')[0]
        
        title = tmp.select('h3 > input[type=hidden]')[0].attrs['value']
        data['title'] = title
        tmpStatus = tmp.select('h3 > em')[0].text
        if tmpStatus == '(모집중)' :
            recruit_status = True
        else :
            recruit_status = False
        data['recruit_status'] = recruit_status
        do_date = tmp.select('div.board_data.type2 > div:nth-child(1) > dl:nth-child(1) > dd')[0].text
        data['do_date'] = do_date
        do_time = tmp.select('div.board_data.type2 > div:nth-child(1) > dl:nth-child(2) > dd')[0].text
        data['do_time'] = do_time
        recruit_date = tmp.select('div.board_data.type2 > div:nth-child(2) > dl:nth-child(1) > dd')[0].text
        data['recruit_date'] = recruit_date
        do_week = tmp.select('div.board_data.type2 > div:nth-child(2) > dl:nth-child(2) > dd')[0].text
        data['do_week'] = do_week
        recruit_member = tmp.select('div.board_data.type2 > div:nth-child(3) > dl:nth-child(1) > dd')[0].text
        data['recruit_member'] = recruit_member
        domain = tmp.select('div.board_data.type2 > div:nth-child(4) > dl:nth-child(1) > dd')[0].text
        data['domain'] = domain
        adult_tmp = tmp.select('div.board_data.type2 > div:nth-child(4) > dl:nth-child(2) > dd')[0].text.strip()
        data['adult_status'] = adult_tmp
        company_tmp = tmp.select('div.board_data.type2 > div:nth-child(5) > dl:nth-child(1) > dd')
        if len(company_tmp) <= 1 :
            data['recruit_company'] = company_tmp[0].text.strip()
        else :
            data['recruit_company'] = company_tmp[0].select('span')[0].text

        data['text'] = tmp.select('div.board_body > div.bb_txt > pre')[0].text
        data['telephone'] = tmp.select('div.board_body > div.incharge_data > dl.tel > dd')[0].text
        address_temp = tmp.select('#dataAdres')[0].text.strip().split(' ')
        data['address_city'] = address_temp[0]
        data['address_gu'] = address_temp[1]
        data['address_remainder'] = ''
        for j in range(2,len(address_temp)) :
            data['address_remainder'] += address_temp[j]
            if j != len(address_temp)-1 :
                data['address_remainder'] += ' '

        result.append(data)
    
    return result


if __name__ == '__main__' :
    datas = parser_1365()
    for data in datas :
        Post(
            regist_no = data['regist_no'],
            title = data['title'],
            recruit_status = data['recruit_status'],
            adult_status = data['adult_status'],
            domain = data['domain'],
            text = data['text'],
            do_date = data['do_date'],
            do_time = data['do_time'],
            do_week = data['do_week'],
            recruit_date = data['recruit_date'],
            recruit_member = data['recruit_member'],
            recruit_company = data['recruit_company'],
            telephone = data['telephone'],
            address_city = data['address_city'],
            address_gu = data['address_gu'],
            address_remainder = data['address_remainder']
        ).save()