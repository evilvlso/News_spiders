#!/bin/env python3
#  coding : utf-8

from collections import defaultdict
import pymongo
class News(object):
    def __init__(self):
        self.global_news=defaultdict(list)
        self.db=self.connect_db()
    def connect_db(self):
        client=pymongo.MongoClient(host='123.206.82.71',port=2232)
        client.admin.authenticate('root','redhat')
        db=client.spiders
        return db
    def query(self,keyword):
        if self.db is  not None:
            collection=self.db[keyword]
        else :
            return None
        result=collection.find().sort('date',pymongo.ASCENDING).limit(10)
        for res in result:
            self.global_news[keyword].append((res['title'],res['link']))
        
if __name__ == '__main__':
    news=News()
    news.query('baidunews')
    info=news.global_news.get('baidunews')
    print(info)
    