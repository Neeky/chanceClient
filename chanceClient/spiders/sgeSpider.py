# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

class GlodPriceItem(scrapy.Item):
    contract   =scrapy.Field()
    highest    =scrapy.Field()
    lowest     =scrapy.Field()
    opening    =scrapy.Field()
    closing    =scrapy.Field()

    def convert(self):
        datas=dict(self)
        res  ={}
        res['contract'] =datas['contract'][0].strip() if datas['contract'][0] != None else 'Au99.99'
        res['highest']  =float(datas['highest'][0])   if datas['highest'][0]  != '-' else -1
        res['lowest']   =float(datas['lowest'][0])    if datas['lowest'][0]   != '-' else -1
        res['opening']  =float(datas['opening'][0])   if datas['opening'][0]  != '-' else -1
        res['closing']  =float(datas['closing'][0])   if datas['closing'][0]  != '-' else -1
        return res

class SgespiderSpider(scrapy.Spider):
    name = 'sgeSpider'
    allowed_domains = ['www.sge.com.cn']
    start_urls = ['https://www.sge.com.cn/hqsj']
    def parse(self, response):
        gpil=ItemLoader(item=GlodPriceItem(),response=response)
        auXpath='//div/descendant::table[position()=1]/descendant::tr[position()=1]' 
        gpil.add_xpath('contract',auXpath +'//td[position()=1]/text()')
        gpil.add_xpath('opening' ,auXpath +'//td[position()=2]/text()')
        gpil.add_xpath('closing' ,auXpath +'//td[position()=3]/text()')
        gpil.add_xpath('highest' ,auXpath +'//td[position()=4]/text()')
        gpil.add_xpath('lowest'  ,auXpath +'//td[position()=5]/text()')
        return gpil.load_item()
