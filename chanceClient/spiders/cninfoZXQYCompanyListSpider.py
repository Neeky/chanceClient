# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

class CompanyListItem(scrapy.Item):
    stockCodeAndName=scrapy.Field()
    infoPage =scrapy.Field()

class CninfozxqycompanylistspiderSpider(scrapy.Spider):
    name = 'cninfoZXQYCompanyListSpider'
    allowed_domains = ['www.cninfo.com.cn']
    start_urls = ['http://www.cninfo.com.cn/cninfo-new/information/companylist']

    def parse(self, response):
        zxqyil=ItemLoader(item=CompanyListItem(),response=response)
        zxqyil.add_xpath('stockCodeAndName',"//div[@id='con-a-2']/descendant::a/text()")
        zxqyil.add_xpath('infoPage'        ,"//div[@id='con-a-2']/descendant::a/@href")
        return zxqyil.load_item()
