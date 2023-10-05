import pandas as pd
import numpy as np

import params as pa

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

waitseconds = 10
def driversetting(Path):    #무슨 파일 받는지 모르니깐 청소를 해주는 함수

    options =  webdriver.ChromeOptions()
    options.add_experimental_option( )

    if 1:
       options.add_argument('headless')

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable path=pa.CHROME_DRIVER_PATH, options=options)
    driver.implicitly_wait(waitseconds)

    return[]

def gen(TargetDay,Farm,Method):
    DownloadPath = r"\Users\aude3\Downloads\Advanced"

    return []

if __name__ == '__main__':
