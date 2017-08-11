# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

class ShiborRateItem(scrapy.Item):
    pushDate   =scrapy.Field()
    oneNight   =scrapy.Field()
    oneWeek    =scrapy.Field()
    twoWeek    =scrapy.Field()
    oneMonth   =scrapy.Field()
    threeMonth =scrapy.Field()
    sixMonth   =scrapy.Field()
    nineMonth  =scrapy.Field()
    oneYear    =scrapy.Field()

    def convert(self):
        datas=dict(self)
        res={}
        res['pushDate']  =datas['pushDate'][0].strip()
        res['oneNight']  =float(datas['oneNight'][0])
        res['oneWeek']   =float(datas['oneWeek'][0])
        res['twoWeek']   =float(datas['twoWeek'][0])
        res['oneMonth']  =float(datas['oneMonth'][0])
        res['threeMonth']=float(datas['threeMonth'][0])
        res['sixMonth']  =float(datas['sixMonth'][0])
        res['nineMonth'] =float(datas['nineMonth'][0])
        res['oneYear']   =float(datas['oneYear'][0])
        return res

class ShiborspiderSpider(scrapy.Spider):
    name = 'shiborSpider'
    allowed_domains = ['www.shibor.org']
    start_urls = ['http://www.shibor.org/shibor/web/html/shibor.html#']

    def parse(self, response):
        sbil=ItemLoader(item=ShiborRateItem(),response=response)
        xpathTb3='//div/descendant::table[position()=1]/descendant::table[position()=3]'
        sbil.add_xpath('pushDate','//div/descendant::table[position()=1]/descendant::table[position()=1]'
                                  '//td[position()=1]/text()')
        sbil.add_xpath('oneNight'  ,xpathTb3 +'//tr[position()=1]/td[position()=3]/text()')
        sbil.add_xpath('oneWeek'   ,xpathTb3 +'//tr[position()=2]/td[position()=3]/text()')
        sbil.add_xpath('twoWeek'   ,xpathTb3 +'//tr[position()=3]/td[position()=3]/text()')
        sbil.add_xpath('oneMonth'  ,xpathTb3 +'//tr[position()=4]/td[position()=3]/text()')
        sbil.add_xpath('threeMonth',xpathTb3 +'//tr[position()=5]/td[position()=3]/text()')
        sbil.add_xpath('sixMonth'  ,xpathTb3 +'//tr[position()=6]/td[position()=3]/text()')
        sbil.add_xpath('nineMonth' ,xpathTb3 +'//tr[position()=7]/td[position()=3]/text()')
        sbil.add_xpath('oneYear'   ,xpathTb3 +'//tr[position()=8]/td[position()=3]/text()')
        print(sbil.load_item().convert())
        pass
