import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from time import sleep
import random
import os
import unicodedata 

driver = webdriver.Chrome('chromedriver')

search_word = input('Keyword: ') #키워드 검색
search_n = input('Post_Number: ') #크롤링할 포스트 갯수 지정

baseUrl = 'https://www.instagram.com/explore/tags/' + search_word + '/'

driver.implicitly_wait(5)

front_url = 'https://www.instagram.com/'
driver.get(front_url)
# to input ID
driver.find_element_by_name('username').send_keys('아이디입력')

# to input password
driver.find_element_by_name('password').send_keys('비밀번호 입력')

# login button click
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
sleep(2)

# click the button in the page after login page
clicker = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
clicker.click()
sleep(2)

driver.get(baseUrl)

driver.find_elements_by_css_selector('._9AhH0')[0].click() #첫번째 게시글 클릭
# tags = driver.find_elements_by_css_selector('.xil3i') 

n = 1

while True: 
    try:
        if int(search_n) > n:
            sleep(4)

            #포스트 게시글 파싱
            test = driver.find_element_by_css_selector(".XQXOT .C4VMK")
            table_html = test.get_attribute('innerHTML')
            soup = BeautifulSoup(table_html, 'html.parser')
            content_html = str(soup.select('span')[-1])
            # print("첫번째content_html: ",content_html)
            sleep(2)

            # # 작성글에서 앞, 뒤의 span부분 제거
            pattern2 = re.compile(r"<span class.+?>")
            content_html = re.sub(pattern2, "", content_html)
            content_html = content_html.replace("</span>", "")
            # print("두번쨰content_html: ",content_html)

            # # 작성글에서 </br> 제거
            pattern3 = re.compile(r"<br/>")
            br_list = re.findall(pattern3, content_html)
            # print("brlist: ",br_list)
            for br in br_list:
                content_html = content_html.replace(br, " ")
            # print("세번째content_html: ",content_html)
            
            # # 작성글에서 </a> 제거
            pattern4 = re.compile(r"<a class.+?>")
            content_html = re.sub(pattern4, "", content_html)
            content_html = content_html.replace("</a>", "")
            # print("네번째content_html: ",content_html)

            save_file_path_hash = "./Hashtag_IPC/패션/" + str(search_word) + '.txt' #경로지정
            f = open(save_file_path_hash, 'a', encoding='utf-8', newline="")

            uni1 = unicodedata.normalize('NFD',content_html) #자모음 분리
            uni2 = unicodedata.normalize('NFC',uni1) #자모음 재합성
            f.write(uni2)
            f.write('\n')
            n+=1
            print(str(search_word),n,'번째post')

            driver.find_element_by_link_text('다음').click() #다음 포스트 클릭
                    
        else:
            if n >= int(search_n): #search_n 입력값만큼 크롤링을 하였다면 크롤링 중지
                break

            else:
                driver.execute_script('windows.scrollTo(0, document.body.scrollHeight)') #화면 스크롤 조정
    
    except:
        pass
driver.close()
print("크롤링완료")
