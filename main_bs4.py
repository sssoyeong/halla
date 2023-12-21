import os
os.environ['CURL_CA_BUNDLE']=''

import sys
import time
import urllib3
import requests
# from playsound import playsound
from bs4 import BeautifulSoup
from selenium import webdriver


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://visithalla.jeju.go.kr/reservation/status.do'

while True:
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        count_26 = int(soup.select_one('#TD_20231226 > a > div > div > span').get_text(strip=True))
        count_27 = int(soup.select_one('#TD_20231227 > a > div > div > span').get_text(strip=True))
        if (count_26 < 2) | (count_27 < 2):
            print(f'{time.strftime("[%y%m%d %H:%M:%S]")} : not found')
        else:
            print(f'{time.strftime("[%y%m%d %H:%M:%S]")} : F O U N D ')
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            if sys.platform == 'darwin':
                chrome_options.add_argument('--start-maximized')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            break
