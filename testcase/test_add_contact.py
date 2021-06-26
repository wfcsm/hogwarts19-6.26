import time

import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddContact:
    def setup(self):
        # options = Options()
        # options.debugger_address='127.0.0.1:9223'
        #
        # self.driver = webdriver.Chrome(executable_path='../driver/chromedriver',options=options)
        self.driver = webdriver.Chrome(executable_path='../driver/chromedriver')
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def test_set_cookies(self):
        self.driver.get(url='https://work.weixin.qq.com/wework_admin/frame#contacts')
        self.cookies = self.driver.get_cookies()
        with open(file='../datas/cookie.yaml',mode='w') as f:
            yaml.safe_dump(data=self.cookies, stream=f)



    def test_add(self):
        self.driver.get(url='https://work.weixin.qq.com/wework_admin/frame#contacts')
        with open(file='../datas/cookie.yaml',mode='r') as f:
            cookies_dict = yaml.safe_load(f)
        for cookie in cookies_dict:
            self.driver.add_cookie(cookie)
            
        self.driver.get(url='https://work.weixin.qq.com/wework_admin/frame#contacts')

        action=ActionChains(self.driver)
        # add_member=WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[@class='ww_operationBar']/a[text()='添加成员']")))
        time.sleep(10)
        add_member=self.driver.find_element(By.XPATH,"//div[@class='ww_operationBar']/a[1]")
        action.click(add_member)
        action.perform()
        # username = WebDriverWait(self.driver, 20).until(
        #         EC.presence_of_element_located((By.ID, "'username")))
        # username.send_keys(str(time.time()))
        # form 表单提交
        self.driver.find_element(By.ID,'username').send_keys(str(time.time()))
        self.driver.find_element(By.ID,'memberAdd_english_name').send_keys(str(time.time()))
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys('zyc')
        self.driver.find_element(By.ID,'memberAdd_phone').send_keys('13429651912')
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()


