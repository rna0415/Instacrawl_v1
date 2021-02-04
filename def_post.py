# credit to our lab member Yoseop Ahn http://cpslab.skku.edu/people-Ahn-Yoseop.php

import requests
import re
from selenium import webdriver
from time import sleep
from openpyxl import load_workbook
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
from bs4 import BeautifulSoup
import csv
import time
import re
import random

# 개발에 쓰일 인스타그램 게시글 전체 탐색_계정당 모든 사진, 영상들 url을 가져오는 함수
# 중간에 렉이 걸리면 처음부터 다시 시작한다.
def count_func(body):
    while True:
        while True:

            # press PageDown button 5times
            body.send_keys(Keys.PAGE_DOWN)
            sleep(random.random() * 6)

            test = driver.find_element_by_css_selector("._2z6nI")
            table_html = test.get_attribute('innerHTML')
            soup = BeautifulSoup(table_html, 'html.parser')
            pictures_html = soup.select('.Nnq7C .v1Nh3 a[href]')

            for content in pictures_html:
                picture_url = "https://www.instagram.com" + content['href']

                if picture_url in picture_urls:
                    continue
                else:
                    picture_urls.append(picture_url)

            # 로드중에 렉이 걸리면 계속 사진 카운트가 같은 숫자로만 나온다.
            # 그래서 10번 이상 같은 숫자가 나오면 처음부터 다시 시작하도록 한다.
            count_num_list.append(len(picture_urls))
            print(count_num_list.count(count_num_list[-1]))
            if count_num_list.count(count_num_list[-1]) > 10:
                driver.get(page_url)
                sleep(5)
                break

            print(len(picture_urls), ' / ', posting_count)


            if posting_count - 5 <= len(picture_urls) and len(picture_urls) <= posting_count:

                for _ in range(0, 3):
                    body = driver.find_element_by_css_selector('body')

                    # press PageDown button 5times
                    body.send_keys(Keys.PAGE_DOWN)
                    sleep(3)

                    test = driver.find_element_by_css_selector("._2z6nI")
                    table_html = test.get_attribute('innerHTML')
                    soup = BeautifulSoup(table_html, 'html.parser')
                    pictures_html = soup.select('.Nnq7C .v1Nh3 a[href]')

                    for content in pictures_html:
                        picture_url = "https://www.instagram.com" + content['href']

                        if picture_url in picture_urls:
                            continue
                        else:
                            picture_urls.append(picture_url)

                    # print(picture_urls)
                    print(len(picture_urls), ' / ', posting_count)

                return
