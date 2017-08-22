# -*- coding: utf-8 -*-
import scrapy


class PbcmoneysupplySpider(scrapy.Spider):
    name = 'pbcMoneySupply'
    allowed_domains = ['www.pbc.org.cn']
    start_urls = ['http://www.pbc.gov.cn/diaochatongjisi/resource/cms/2017/07/2017071716280457665.htm']

    def parse(self, response):
        print(response.text)
        pass
