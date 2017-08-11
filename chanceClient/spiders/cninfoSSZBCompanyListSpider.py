# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

class CompanyListItem(scrapy.Item):
    stockCodeAndName=scrapy.Field()
    infoPage =scrapy.Field()

class CninfosszbcompanylistspiderSpider(scrapy.Spider):
    name = 'cninfoSSZBCompanyListSpider'
    allowed_domains = ['www.cninfo.com.cn']
    start_urls = ['http://www.cninfo.com.cn/cninfo-new/information/companylist']

    def parse(self, response):
        #深市主板
        sszbil=ItemLoader(item=CompanyListItem(),response=response)
        sszbil.add_xpath('stockCodeAndName'    ,"//div[@id='con-a-1']/descendant::a/text()")
        sszbil.add_xpath('infoPage'            ,"//div[@id='con-a-1']/descendant::a/@href")
        return sszbil.load_item()
