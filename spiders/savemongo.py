#!/bin/env python3
#  coding : utf-8
import pymongo
import datetime
def savedata(dic,col):
    try:
        client = pymongo.MongoClient(host='123.206.82.71', port=2232)
        client.admin.authenticate('root', 'redhat')
        db = client.spiders
        collections = db[col]
        if collections.insert_one(dic):
            print('存储成功！')
    
    except Exception as e:
        print(e)

def truncate(col):
    client = pymongo.MongoClient(host='123.206.82.71', port=2232)
    client.admin.authenticate('root', 'redhat')
    db = client.spiders
    collections = db[col]
    collections.remove({})
    
def createindex(col):
    client = pymongo.MongoClient(host='123.206.82.71', port=2232)
    client.admin.authenticate('root', 'redhat')
    db = client.spiders
    collections = db[col]
    collections.create_index([('date',pymongo.ASCENDING)],expireAfterSeconds=7200)
if __name__ == '__main__':
    dic={'test':1,'name':355,'date':datetime.datetime.now()}
    savedata(dic=dic,col='test')
    #createindex(col='test')