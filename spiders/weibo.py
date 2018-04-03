#!/bin/env python3
#  coding : utf-8
import requests
import savemongo
from urllib.parse import unquote
import pymongo
import re
import datetime
class weibo_News(object):
    def __init__(self):
        self.url = 'http://s.weibo.com/top/summary?cate=realtimehot'
        
    def getNews(self):
        try:
            response=requests.get(self.url,timeout=5)
            html=response.text
            html=re.findall('<script>(.*?)</script>',html)[-2]
            pattern=re.compile(r'<td class=\\"td_05\\"><a href=\\"\\/weibo\\/(.*?)&Refer=top\\')
            match=re.findall(pattern,html)
            #savemongo.truncate(col='weibonews')
            for con in match:
                dic={}
                dic['title']=unquote(con.replace('25',''))
                dic['link']='http://s.weibo.com/weibo/'+con.replace('25','')
                dic['date']=datetime.datetime.now()
                print(dic)
                savemongo.savedata(dic=dic,col='weibonews')
        except Exception as e:
            print(e)
        
    def cleardatab(self):
        savemongo.truncate(col='weibonews')



if __name__=='__main__':
    
    weibo=weibo_News()
    weibo.getNews()
