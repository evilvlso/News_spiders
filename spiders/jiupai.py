#!/bin/env python3
#  coding : utf-8

import requests
import pymongo
import lxml
import  savemongo
import time
import datetime
from urllib.parse import urlencode

class jiupai_News(object):
    def __init__(self):
        self.init_url='http://appjph.jiupaicn.com/app/content/hot/list?type=1&page=1&pageSize=10&_={timestamp}'
    
    def get_url(self):
        timestamp=str(round(time.time(),3)).replace('.','')
        url=self.init_url.format(timestamp=timestamp)
        return url
    
    def pase_html(self):
        try:
            url=self.get_url()
            res=requests.get(url,timeout=10).json()
            if not res['resultMessage']=='请求处理成功':
                print('获取数据失败')
            else :
                result_list=res.get("resultData")
                savemongo.truncate(col='jiupainews')
                for result in result_list:
                    dic={}
                    params={'catiId':result.get('catId'),
                    'memberId':result.get('memberId'),
                    'id':result.get('id')}
                    dic['title']=result.get('title')
                    dic['link']='http://jphao.jiupaicn.com/index.php?m=content&c=jiupaihao&a=article&{0}'.format(urlencode(params))
                    dic['date']=datetime.datetime.now()
                    
                    savemongo.savedata(dic=dic,col='jiupainews')
                    #print(dic)
        except Exception as e:
            print(e)

    def cleardatab(self):
        savemongo.truncate(col='jiupainews')
 
if __name__=='__main__':
    jiupai=jiupai_News()
    print(jiupai.get_url())
    jiupai.pase_html()
