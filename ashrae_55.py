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


# options = webdriver.ChromeOptions()
# # options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
#
# driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
#
# # driver = webdriver.Chrome('./chromedriver.exe')
# url = 'https://www.ashrae.org/technical-resources/standards-and-guidelines/read-only-versions-of-ashrae-standards'
# driver.get(url)
# time.sleep(100)
# driver.find_element('XPATH', "/html/body/form/div[2]/main/div[4]/div/div/div[1]/div/div/div/p[12]/a").click()

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "./chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

driver.find_element(By.XPATH, '/html/body/app-root[1]/app-home/div[1]/app-foxitpdfviewer/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div/div[6]').screenshot('./test2.png')

# time.sleep(10)
# for i in range(80):
#     driver.find_element(By.XPATH, "//*[@id="pdf_doc_unique_1662362939145_0"]/div[3]/div[1]/div").screenshot('./ashrae_55_' + str(i+1) + '.png')




