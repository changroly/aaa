# -*- coding: utf-8 -*-
from pymongo import MongoClient
import urllib.parse
import datetime
import pymongo
###############################################################################
#                       股票機器人 Python基礎教學 【pymongo教學】                      #
###############################################################################

# Authentication Database認證資料庫
Authdb='bot'

##### 資料庫連接 #####
def constructor():
    client = MongoClient('mongodb://roly:dayi3774@cluster0-shard-00-00.0mtts.mongodb.net:27017,cluster0-shard-00-01.0mtts.mongodb.net:27017,cluster0-shard-00-02.0mtts.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-da52w8-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = client[Authdb]
    return db
   
#----------------------------儲存使用者的股票--------------------------
def write_user_stock_fountion(stock, bs, price):  
    db=constructor()
    collect = db['mystock']
    collect.insert({"stock": stock,
                    "data": 'care_stock',
                    "bs": bs,
                    "price": float(price),
                    "date_info": datetime.datetime.utcnow()
                    })
    
#----------------------------殺掉使用者的股票--------------------------
def delete_user_stock_fountion(stock):  
    db=constructor()
    collect = db['mystock']
    collect.remove({"stock": stock})
    
#----------------------------秀出使用者的股票--------------------------
def show_user_stock_fountion():  
    db=constructor()
    collect = db['mystock']
    cel=list(collect.find({"data": 'care_stock'}))

    return cel



