import os
os.environ['CURL_CA_BUNDLE']=''

import sys
import time
import urllib3
import requests
# from playsound import playsound
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://visithalla.jeju.go.kr/reservation/status.do'

while True:
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        count_26 = int(soup.select_one('#TD_20231226 > a > div > div > span').get_text(strip=True))
        count_27 = int(soup.select_one('#TD_20231227 > a > div > div > span').get_text(strip=True))
        # if (count_26 < 1) & (count_27 < 1):
        if count_26 < 1:
            print(f'{time.strftime("[%y%m%d %H:%M:%S]")} : not found')
        else:
            print(f'{time.strftime("[%y%m%d %H:%M:%S]")} : F O U N D ')
            print(f'26일: {count_26}, 27일: {count_27}')
            print(url)
            
            if count_26 < 1:
                url_rsv = 'https://visithalla.jeju.go.kr/reservation/firstComeStep.do?visitDt=2023.12.26&courseSeq=242&cmpaCnt=1'
            else:
                url_rsv = 'https://visithalla.jeju.go.kr/reservation/firstComeStep.do?visitDt=2023.12.27&courseSeq=242&cmpaCnt=1'
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url_rsv)
            break
        