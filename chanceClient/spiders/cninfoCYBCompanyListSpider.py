# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from .cninfo import CompanyListItem

"""
class CompanyListItem(scrapy.Item):
    stockCodeAndName=scrapy.Field()
    infoPage =scrapy.Field()
"""
class CninfosszbcompanylistspiderSpider(scrapy.Spider):
    name = 'cninfoCYBCompanyListSpider'
    allowed_domains = ['www.cninfo.com.cn']
    start_urls = ['http://www.cninfo.com.cn/cninfo-new/information/companylist']

    def parse(self, response):
        #创业板
        cybil=ItemLoader(item=CompanyListItem(),response=response)
        cybil.add_xpath('stockCodeAndName'    ,"//div[@id='con-a-3']/descendant::a/text()")
        cybil.add_xpath('infoPage'            ,"//div[@id='con-a-3']/descendant::a/@href")
        return cybil.load_item()
