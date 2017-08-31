# -*- coding: utf-8 -*-
import scrapy
from   chanceClient.items import IndexOverview 

def linesToDict(lines):
    res={}
    for line in lines:
        if '=' in line:
            k,v=line.replace('var','').split('=')
            k=k.strip()
            v=v.replace('"','').replace('\r','')
            res[k]=v
    return res

kvMap={
    #'pushDate':'zsgz00',
    #           静态市盈率    ,动态市盈率,   ,市净率       ,股息率
    '上证指数':{'spe':'zsgz11','dpe':'zsgz12','pb':'zsgz13','dp':'zsgz18'},
    '上证180' :{'spe':'zsgz21','dpe':'zsgz22','pb':'zsgz23','dp':'zsgz28'},
    '上证50'  :{'spe':'zsgz31','dpe':'zsgz32','pb':'zsgz33','dp':'zsgz38'},
    '沪深300' :{'spe':'zsgz41','dpe':'zsgz42','pb':'zsgz43','dp':'zsgz48'},
    '深证成指':{'spe':'zsgz51','dpe':'zsgz52','pb':'zsgz53','dp':'zsgz58'},
    '深证100R':{'spe':'zsgz61','dpe':'zsgz62','pb':'zsgz63','dp':'zsgz68'},
    '中小板指':{'spe':'zsgz71','dpe':'zsgz72','pb':'zsgz73','dp':'zsgz78'},
    '上证380' :{'spe':'zsgz81','dpe':'zsgz82','pb':'zsgz83','dp':'zsgz88'},
    '红利指数':{'spe':'zsgz91','dpe':'zsgz92','pb':'zsgz93','dp':'zsgz98'},
    '中证红利':{'spe':'zsgz101','dpe':'zsgz102','pb':'zsgz103','dp':'zsgz108'},
    '中证500' :{'spe':'zsgz111','dpe':'zsgz112','pb':'zsgz113','dp':'zsgz118'}
}

def genItem(kvs,indexName):
    item             = IndexOverview()
    item['pushDate'] =kvs['zsgz00']
    item['indexName']=indexName
    current=kvMap[indexName]
    spe    =current['spe']
    dpe    =current['dpe']
    pb     = current['pb']
    dp     = current['dp']
    item['spe']=kvs[spe]
    item['dpe']=kvs[dpe]
    item['pb'] =kvs[pb]
    item['dp'] =kvs[dp]
    return item

class CsindexspiderSpider(scrapy.Spider):
    name = 'csindexSpider'
    allowed_domains = ['www.csindex.com.cn']
    start_urls = ['http://www.csindex.com.cn/data/js/show_zsgz.js?str=z3l50GN6FTsOxMrb']

    def parse(self, response):
        res=linesToDict(response.text.split('\n'))
        for k in kvMap:
            yield genItem(res,k)









