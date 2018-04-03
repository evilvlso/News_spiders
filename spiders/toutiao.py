#!/bin/env python3
#  coding : utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import requests
import time
import datetime
import savemongo
#chromoptions=webdriver.ChromeOptions()
#chromoptions.add_argument('--headless')

#browser=webdriver.Chrome(chrome_options=chromoptions)

#browser.get('https://s.taobao.com/search?q=%E6%80%A7%E6%84%9F%E6%83%85%E8%B6%A3')
#source_page=browser.page_source

class toutiao_News(object):
    def __init__(self):
        self.chrome=webdriver.ChromeOptions()
        self.chrome.add_argument('--headless')
        self.browser=webdriver.Chrome(chrome_options=self.chrome)
        self.wait=WebDriverWait(self.browser,10)
    def get_source(self):
        self.browser.get('https://www.toutiao.com/')
        source_html=self.browser.page_source
        return source_html
        
    def __del__(self):
        self.browser.close()
    def parse_html(self,page=1):
        page_source = self.get_source()
        for page in range(1,page+1):
            if page>1:
                self.browser.execute_script("window.scrollBy(0,document.body.scrollHeight=10000)", "")
                self.browser.execute_script("window.scrollBy(0,document.body.scrollTop)", "")
                self.browser.execute_script("window.scrollBy(0,document.body.scrollTop)", "")
                #self.wait.until(EC.text_to_be_present_in_element_value((By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div[3]"),"display"))
                #ac = self.browser.find_element_by_xpath("//ul[@infinite-scroll-disabled]/li[last()]")
                #ac.location_once_scrolled_into_view
                #self.wait.until(EC.visibility_of_element_located((By.XPATH,"//ul[@infinite-scroll-disabled]/li[last()]")))
                time.sleep(3)
                page_source=self.browser.page_source
            
            html=etree.HTML(page_source)
            element_list=html.xpath('//ul[@infinite-scroll-disabled]/li/div[@ga_event="article_item_click"]')
            present_list_num=len(element_list)
            if page>1:
                element_list = element_list[pre_list_num:]
            pre_list_num = present_list_num
            
            for element in element_list:
                dic={}
                dic['title']=element.xpath('.//div[@class="title-box"]/a/text()')[0]
                dic['link']='https://www.toutiao.com/'+element.xpath('.//div[@class="title-box"]/a/@href')[0]
                dic['date']=datetime.datetime.now()
                print(dic)
                #savemongo.savedata(dic=dic,col='toutiaonews')
    def shutdown(self):
        self.browser.close()
if __name__=='__main__':
        toutiao=toutiao_News()
        toutiao.parse_html(4)
    