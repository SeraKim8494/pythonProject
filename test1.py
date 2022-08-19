from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#from bs4 import beautifulsoup


driver = webdriver.Chrome('/Users/serakim/Downloads/chromedriver')

driver.get("https://www.google.com/maps/")
driver.implicitly_wait(10)


driver.find_element("name", 'q').send_keys('카페')
driver.find_element("id", 'searchbox-searchbutton').click() #브라우저 열고 '카페' 입력 후 검색 버튼 클릭

time.sleep(5)

stores = driver.find_elements("css selector", '.bfdHYd.Ppzolf.OFBs3e')


for s in stores:
    title = s.find_element("css selector", '.NrDZNb').text

    try:
        score = s.find_element("css selector", '.MW4etd').text

    except:
        score = "평점없음"

    addr = s.find_element("css selector", 'div:nth-child(2) > span:nth-child(2) > jsl > span:nth-child(2)').text

    print(title, "/", score, "/", addr)

driver.close()