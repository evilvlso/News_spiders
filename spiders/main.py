#!/bin/env python3
#  coding : utf-8
import os
from threading import Thread
from baidu import BaiduNEWS
from jiupai import jiupai_News
from toutiao import toutiao_News
from weibo import weibo_News
import savemongo
def baiduThread():
    baidunews = BaiduNEWS()
    baidunews.getnews()
def toutiaoThread():
    try:
        toutiao = toutiao_News()
        toutiao.parse_html(3)
    finally:
        toutiao.shutdown()
        os.popen('ps -ef  | grep chrome | grep -v grep|awk -F " " \'{print "kill -9 " $2}\'| sh')
def jiupaiThread():
    jiupai = jiupai_News()
    jiupai.pase_html()
def weiboThread():
    weibo = weibo_News()
    weibo.getNews()
def printinfo():
    print('this is woca')

if __name__ == '__main__':

    t = Thread(target=baiduThread)
    t.start()
    t.join()
    t2= Thread(target=toutiaoThread)
    t2.start()
    t2.join()
    t3 = Thread(target=jiupaiThread)
    t3.start()
    t3.join()
    t4 = Thread(target=weiboThread)
    t4.start()
    t4.join()
    print('its   over!!!')