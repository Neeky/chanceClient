# -*- coding: utf-8 -*-
import scrapy

from   chanceClient.items import IndexDetail

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
    '上证指数':{'close':'zsbx11','delta':'zsbx12','deltaPercent':'zsbx13'},
    '上证180' :{'close':'zsbx21','delta':'zsbx22','deltaPercent':'zsbx23'},
    '上证50'  :{'close':'zsbx31','delta':'zsbx32','deltaPercent':'zsbx33'},
    '沪深300' :{'close':'zsbx41','delta':'zsbx42','deltaPercent':'zsbx43'},
    '深证成指':{'close':'zsbx51','delta':'zsbx52','deltaPercent':'zsbx53'},
    '深证100R':{'close':'zsbx61','delta':'zsbx62','deltaPercent':'zsbx63'},
    '中小板指':{'close':'zsbx71','delta':'zsbx72','deltaPercent':'zsbx73'},
    '上证380' :{'close':'zsbx81','delta':'zsbx82','deltaPercent':'zsbx83'},
    '红利指数':{'close':'zsbx91','delta':'zsbx92','deltaPercent':'zsbx93'},
    '中证红利':{'close':'zsbx101','delta':'zsbx102','deltaPercent':'zsbx103'},
    '中证500' :{'close':'zsbx111','delta':'zsbx112','deltaPercent':'zsbx113'}
}

def genIndexDetailItem(indexname,res):
    pushDate=res['zsbx00']
    current=kvMap[indexname]
    closeValue=current['close']
    delta     =current['delta']
    deltaPercent=current['deltaPercent']
    item=IndexDetail()
    item['pushDate']=pushDate
    item['indexName']=indexname
    item['closeValue']=res[closeValue]
    item['delta']= res[delta]
    item['deltaPercent']=res[deltaPercent]
    return item

class CsindexdetailspiderSpider(scrapy.Spider):
    name = 'csindexDetailSpider'
    allowed_domains = ['www.csindex.com.cn']
    start_urls = ['http://www.csindex.com.cn/data/js/show_zsbx.js?str=SF2Qo2Jp32GgA3jJ']

    def parse(self, response):
        variables=linesToDict(response.text.split('\n'))
        for indexname in kvMap:
            yield genIndexDetailItem(indexname,variables)









