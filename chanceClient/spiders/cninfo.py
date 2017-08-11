# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

class CompanyListItem(scrapy.Item):
    stockCodeAndName=scrapy.Field()
    infoPage =scrapy.Field()

    def convert(self):
        datas=dict(self)
        res  =[]
        for index in range(len(datas['stockCodeAndName'])):
            stockCode=datas['stockCodeAndName'][index][0:6].strip()
            name=datas['stockCodeAndName'][index][7:]
            infoPage=datas['infoPage'][index]
            res.append({'stockCode':stockCode,'name':name,'infoPage':infoPage})
        return res 
