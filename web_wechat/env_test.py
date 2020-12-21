#coding =utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://work.weixin.qq.com/')
driver.quit()
#使用remote复用浏览器，chrome的debug模式


#使用cookies 跳过登录 