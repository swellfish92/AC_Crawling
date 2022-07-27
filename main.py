import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

# def generate_ym_arr(start_date, end_date):
#     stt_arr = start_date.split('/')
#     end_arr = end_date.split('/')
#     year_diff = end_arr[0] - stt_arr[0]
#     month_diff = end_arr[1] - stt_arr[1]
#     total_diff = year_diff * 12 + month_diff
#     temp_arr = []
#     for i in range(total_diff/3):
#
#         search_str =
#         temp_arr.append()


keyword_arr = ['냉방기']
start_date = '2018/07/27'
end_date = '2022/07/27'



for keyword in keyword_arr:
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://www.g2b.go.kr:8067/contract/TcontSearch.jsp?upmu_gubun=%B9%B0%C7%B0'
    driver.get(url)
    time.sleep(20)
    driver.find_element('id', "tab_bid_03").click()
    driver.find_element('id', "bidNm4").send_keys(keyword)
    driver.find_element('id', "fromBidDt4").send_keys('20220527')
    driver.find_element('id', "toBidDt4").send_keys('20220727')
    driver.find_element('id', "area4").send_keys('국가기관')
    driver.find_element('xpath', "/html/body/div/div[1]/div[1]/div[1]/dl/dd[3]/form/div/fieldset[1]/ul/li[4]/dl/dd[2]/a").click()
    time.sleep(10)