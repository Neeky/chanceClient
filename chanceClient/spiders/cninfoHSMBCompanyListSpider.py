# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from .cninfo import CompanyListItem

class CninfohsmbcompanylistspiderSpider(scrapy.Spider):
    name = 'cninfoHSMBCompanyListSpider'
    allowed_domains = ['www.cninfo.com.cn']
    start_urls = ['http://www.cninfo.com.cn/cninfo-new/information/companylist']

    def parse(self, response):
        #沪市主板
        hszbil=ItemLoader(item=CompanyListItem(),response=response)
        hszbil.add_xpath('stockCodeAndName',"//div[@id='con-a-4']/descendant::a/text()")
        hszbil.add_xpath('infoPage'        ,"//div[@id='con-a-4']/descendant::a/@href")
        return hszbil.load_item()
