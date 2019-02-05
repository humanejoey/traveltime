# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TravelTime:
    def __init__(self):
        self.browser = self.setup_browser()
        self.table = []
        self.fill_table()
        self.browser.quit()

    def setup_browser(self):
        options = Options()
        #options.add_argument("--headless")
        path = "C:/Users/jhunyeom/Desktop/coding/webdrivers/chromedriver.exe"
        browser = webdriver.Chrome(options=options, executable_path=path)
        return browser

    def fill_table(self):
        self.get_data()

    def write_line(self):
        pass

    def get_data(self):
        url = u"https://search.naver.com/search.naver?query=부산장안고에서+서울시청"
        self.browser.get(url.encode('utf-8'))
        self.browser.find_element_by_xpath('//*[@id="raa2"]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="_fasttrack"]/div[1]/div/div/div[2]/button').click()
        time.sleep(1)
        time_str = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="_fasttrack"]/div[2]/div/div[5]/div/strong[1]'))
        ).text
        time_int = self.get_time_from_text(time_str)
        print time_int

    def get_time_from_text(self, text):
        text_list = text.encode('utf-8').split()
        if len(text_list) == 1:
            hour = 0
            minute = int(text_list[0][:-3])
        else:
            hour = int(text_list[0][:-6])
            minute = int(text_list[1][:-3])
        duration = hour*60 + minute
        return duration


TravelTime()
