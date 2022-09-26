import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import datetime
import pandas as pd

# 학습을 위한 코멘트
# 1. 주석 처리
# 주석설정은 ctrl+/ 로 한번에 가능 (커서 있는 줄, 블록선택한 구역 전체 둘 다 가능)
# 그 외는 ''' 를 사용하는 동일한 방법임
# 2. 라이브러리 설치 설정
# 인터프리터 설정 (라이브러리 설치) 단축키는 ctrl+alt+s
# 안되면 하단 좌측의 Terminal 메뉴에서 pip install [라이브러리명] 커맨드로 설치 가능

# 코드백업용 메모
# [401015]
# 환기용기기
# [401016]
# 공기순환장치및액세서리
# [401017]
# 냉방장치
# [401018]
# 난방기구및액세서리
# [401019]
# 습도조절장치
# [401020]
# 보일러
#
# 냉방기
# 40101701
# 환풍냉방장치
# 40101702
# 증발냉방장치
# 40101703
# 축열냉방시스템
# 40101794

# 원래의 조달청 주소 사용을 위해(메뉴가 다 있는 버전) ID코드가 포함된 검색기준 코드를 백업함.
# 나중에 문제가 생긴다면 이 코드 + 조달청 대표 웹 주소로 돌아가면 됨.
# driver.find_element('id', "tab_bid_03").click()
# driver.find_element('id', "bidNm4").send_keys(keyword)
# driver.find_element('id', "fromBidDt4").send_keys('20220527')
# driver.find_element('id', "toBidDt4").send_keys('20220727')
# driver.find_element('id', "area4").send_keys('국가기관')
# driver.find_element('xpath', "/html/body/div/div[1]/div[1]/div[1]/dl/dd[3]/form/div/fieldset[1]/ul/li[4]/dl/dd[2]/a").click()

# datetime처럼 돌아가게 만듬...
def generate_ym_arr(start_ym, end_ym):
    start_arr = start_ym.split('/')
    end_arr = end_ym.split('/')
    start_val = int(start_arr[0])*12 + int(start_arr[1])
    end_val = int(end_arr[0])*12 + int(end_arr[1])
    temp_arr = []
    for i in range((end_val-start_val)//3+1):
        temp_arr.append(str((start_val+i*3)//12) +'/'+ str((start_val+i*3)%12).zfill(2) +'/'+ start_arr[2])
    temp_arr.append(end_ym)
    return temp_arr

def item_search(start_date, end_date, pageno):
    key = "owsao31Eak4pE2i8SQkuu6bVXieWxILomFCxifqPQAW4wgbkVJ%2F9X0hIzljulAYMV6KcUZPLla2xAUusk4B1wg%3D%3D"
    url = "http://apis.data.go.kr/1230000/CntrctInfoService/getCntrctInfoListThngDetail?type=json&inqryDiv=1&inqryBgnDt=" + str(start_date) + "&inqryEndDt=" + str(end_date) + "&numOfRows=999&pageNo=" + str(pageno) + "&ServiceKey=" + key
    print(url)
    result = requests.get(url)
    return result.json()

def get_item_list(start_date, end_date):
    # 항목 수 구하기를 위해 일단 한번 서치함
    first_res = item_search(start_date, end_date, 1)
    # 결과에서 항목 수 값을 획득
    total_count = first_res['response']['body']['totalCount']
    # 페이지당 표시수 최대값인 999로 설정했으니, 몇 페이지까지 표시할지를 계산
    page_len = total_count//999 + 1
    # 페이지 넘버에 대해 결과값을 가져와 합침
    temp_list = []
    for i in range(page_len):
        # range로 구해지는 영역은 0부터고, PageNo값은 1부터이므로 1을 더해서 호출하여야 한다.
        search_res = item_search(start_date, end_date, i+1)
        try:
            temp_list = temp_list + search_res['response']['body']['items']
        except:
            temp_list = temp_list.append(search_res['response']['body']['item'])
    return temp_list

def write_txt(filedir, data):
    filedir = filedir.split('.txt')[0] + '_affix_transformed.txt'
    f = open(filedir, 'w')
    f.writelines(data)
    f.close()
    print('File exported')

today = datetime.date.today()
start_date = str(today.year) + str(today.month-3).zfill(2) + str(today.day).zfill(2) +'0000'
end_date = str(today.year) + str(today.month).zfill(2) + str(today.day).zfill(2) +'0000'
data = get_item_list(start_date, end_date)
df = pd.DataFrame(data)
df.to_csv('result.csv', encoding='utf-8 sig')
raise IOError


keyword_arr = ['냉방기']
start_ym = '2018/06/27'
end_ym = '2022/07/27'


search_arr = generate_ym_arr(start_ym, end_ym)

for keyword in keyword_arr:
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://www.g2b.go.kr:8067/contract/TcontSearch.jsp?upmu_gubun=%B9%B0%C7%B0'
    driver.get(url)
    driver.find_element('id', "pummung_name").send_keys(keyword)
    driver.find_element('id', "from_date").click()
    driver.find_element('id', "from_date").send_keys('2022/05/27')
    driver.find_element('id', "to_date").click()
    driver.find_element('id', "to_date").send_keys('2022/07/27')
    driver.find_element('id', "balzu_code").send_keys('국가기관')
    driver.find_element('xpath', "/html/body/div[1]/div[2]/form/div[3]/div/a[1]/img").click()

    time.sleep(10)



