import sys
import time
import re

# from playsound import playsound

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
if sys.platform == 'darwin':
    chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=chrome_options)

url = 'https://visithalla.jeju.go.kr/reservation/status.do'
driver.get(url)

while True:
    count_26 = int(driver.find_element(By.XPATH, '//*[@id="TD_20231226"]/a/div/div/span').text)
    count_27 = int(driver.find_element(By.XPATH, '//*[@id="TD_20231227"]/a/div/div/span').text)
    if (count_26 < 2) | (count_27 < 2):
        driver.refresh()
        driver.implicitly_wait(10)
    else:
        # playsound("alertsound.mp3")

        if count_26 < 1:
            url_rsv = 'https://visithalla.jeju.go.kr/reservation/firstComeStep.do?visitDt=2023.12.26&courseSeq=242&cmpaCnt=1'
        else:
            url_rsv = 'https://visithalla.jeju.go.kr/reservation/firstComeStep.do?visitDt=2023.12.27&courseSeq=242&cmpaCnt=1'
        driver_new = webdriver.Chrome(options=chrome_options)
        driver_new.get(url_rsv)
        driver_new.implicitly_wait(10)

 