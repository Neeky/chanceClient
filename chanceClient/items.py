# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class IndexOverview(scrapy.Item):
    pushDate =scrapy.Field() #发布时间
    indexName=scrapy.Field() #指数名
    spe      =scrapy.Field() #静态市盈率
    dpe      =scrapy.Field() #动态市盈率
    pb       =scrapy.Field() #市净率
    dp       =scrapy.Field() #股息率
    def convert(self):
        res  ={}
        datas=dict(self)
        res['pushDate'] =datas['pushDate']
        res['indexName']=datas['indexName']
        res['spe']      =datas['spe']
        res['dpe']      =datas['dpe']
        res['pb']       =datas['pb']
        res['dp']       =datas['dp']
        return res

class IndexDetail(scrapy.Item):
    pushDate    =scrapy.Field()
    indexName   =scrapy.Field()
    closeValue  =scrapy.Field()
    delta       =scrapy.Field()
    deltaPercent=scrapy.Field()
    def convert(self):
        res={}
        datas=dict(self)
        res['pushDate']    =datas['pushDate']
        res['indexName']   =datas['indexName']
        res['closeValue']  =datas['closeValue']
        res['delta']       =datas['delta']
        res['deltaPercent']=datas['deltaPercent']
        return res


class ChanceclientItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
