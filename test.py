#encoding:utf8
import requests
import time
from selenium import webdriver
from lxml import etree
import re
import csv
import codecs
# import mysql.connector
# db = mysql.connector.connect(host='127.0.0.1', user='root', password='root', port=3306, db='ysh')
# cursor = db.cursor()
browser = webdriver.Chrome()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Cookie': 'JSESSIONID=4599D68D02690B52C24A2F1F9C616BE2'
}
browser.get('http://192.168.10.4:8080')
# print('成功')

time.sleep(5)

browser.find_element_by_id("account").send_keys("13300001111")
browser.find_element_by_id("pass").send_keys("123123")
# browser.find_element_by_id("code_input").send_keys(input("请输入验证码："))

time.sleep(3)

js = "sendVal('')"
browser.execute_script(js)

# browser.get("http://192.168.10.4:8080/user/all/login?account=13300001111&passwd=123123")

# time.sleep(4)

# browser.get("http://192.168.10.4:8080/company/menu.jsp")

# browser.find_element_by_class_name("lijidenglu").click()


