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

search_word = input('Keyword: ')
tag_n = input('Post_Number: ')

baseUrl = 'https://www.instagram.com/explore/tags/' + search_word + '/'

driver.implicitly_wait(5)

front_url = 'https://www.instagram.com/'
driver.get(front_url)
# to input ID
driver.find_element_by_name('username').send_keys('gimamugae1765')

# to input password
driver.find_element_by_name('password').send_keys('alfkzmfak50')

# login button click
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
sleep(2)

# click the button in the page after login page
clicker = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
clicker.click()
sleep(2)

driver.get(baseUrl)

driver.find_elements_by_css_selector('._9AhH0')[0].click()
tags = driver.find_elements_by_css_selector('.xil3i')
#####
# comments = driver.find_elements_by_css_selector('.P9YgZ .C4VMK span')
# test = driver.find_element_by_css_selector(".XQXOT .C4VMK")
# table_html = test.get_attribute('innerHTML')
# soup = BeautifulSoup(table_html, 'html.parser')
# content_html = str(soup.select('span')[-1])
# print("첫번째content_html: ",content_html)
# sleep(2)

# # # 작성글에서 앞, 뒤의 span부분 제거
# pattern2 = re.compile(r"<span class.+?>")
# content_html = re.sub(pattern2, "", content_html)
# content_html = content_html.replace("</span>", "")
# print("두번쨰content_html: ",content_html)

# # # 작성글에서 </br> 제거
# pattern3 = re.compile(r"<br/>")
# br_list = re.findall(pattern3, content_html)
# print("brlist: ",br_list)

# for br in br_list:
#     content_html = content_html.replace(br, " ")
# print("세번째content_html: ",content_html)

# pattern4 = re.compile(r"<a class.+?>")
# content_html = re.sub(pattern4, "", content_html)
# content_html = content_html.replace("</a>", "")
# print("네번째content_html: ",content_html)

# save_file_path_hash = "./Hashtag_IPC/" + str(search_word) + '.txt'
# f = open(save_file_path_hash, 'w', encoding='utf-8-sig', newline="")

# f.write(content_html)
# f.write('\n')
######
# for i in comments:
#     print("댓글은?",i.text)
# comment_list = []
tag_list = []
n = 1

# save_file_path_hash = "./Hashtag_IPC/" + str(search_word) + '.txt'
# f = open(save_file_path_hash, 'w', encoding='utf-8-sig', newline="")

# for i in int(tag_n):
#     print(i.text)
#     tag_list.append(i.text)


while True: 
    try:
        if int(tag_n) > n:
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

            # uni1 = unicodedata.normalize('NFD',content_html) #자모음 분리
            # uni2 = unicodedata.normalize('NFC',uni1) #자모음 재합성
            f.write(content_html)
            f.write('\n')
            n+=1
            print(str(search_word),n,'번째post')

            driver.find_element_by_link_text('다음').click()
                    
        else:
            if n >= int(tag_n):
                break

            else:
                driver.execute_script('windows.scrollTo(0, document.body.scrollHeight)')
    
    except:
        pass
driver.close()
print("크롤링완료")
# print(len(tag_list))
# print(tag_list)
# for taggy in tag_list:
#     f.write(taggy)
#     f.write('\n')

# for commy in comment_list:
#     f1.write(commy)
#     f1.write('\n')
#     print(i, content_html)    
# driver.close()