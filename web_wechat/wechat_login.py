#coding=UTF-8
"""先登录，然后复用，获取cookies存入yaml文件，在读取cookies的文件  达到使用cookie完成登录"""
from selenium import webdriver
import time,yaml

"""#复用浏览器 ，使用命令 打开chrome的调试模式，然后手工打开需要登录的页面，
#2.在使用下面的代码，跳转到 通讯录 应用管理等需要登录才可以进入的页面,就是在已经登录成功的调试模式下的浏览器进行
#自动化代码的操作进入通讯录页面"""


"""复用浏览器，先手工扫码登录成功，执行代码进入添加成员页面"""
"""先手动登录成功，执行以下代码，复用浏览器进入通讯录  获取cookies并保存"""
def chromeAndSavecokie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=opt)
    # driver.get('https://www.baidu.com/')
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    # driver.find_element_by_xpath("//span[text()='添加成员']").click()
    cookies = driver.get_cookies()
    print(cookies)
    with open('data.yaml','w',encoding='utf-8') as f:
        yaml.dump(cookies,f)

def read_cookieAndLogin():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    #进入扫码登录页
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    with open('data.yaml',encoding='UTF-8')as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    #加入cookies进入index首页
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    #在首页直接点击添加成员跳转到添加成员页
    driver.find_element_by_xpath("//span[text()='添加成员']").click()
    driver.find_element_by_id('username').send_keys('测试开发01')
    driver.find_element_by_id('memberAdd_acctid').send_keys('sun001')
    driver.find_element_by_id('memberAdd_phone').send_keys('13100009901')
    driver.find_element_by_xpath("//a[text()='保存']").click()
    time.sleep(3)


if __name__ =='__main__':
    chromeAndSavecokie()
    read_cookieAndLogin()