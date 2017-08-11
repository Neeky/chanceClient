# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

class CompanyListItem(scrapy.Item):
    stockCodeAndName=scrapy.Field()
    infoPage =scrapy.Field()

