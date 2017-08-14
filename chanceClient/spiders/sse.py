# -*- coding: utf-8 -*-
import scrapy

class SseOverviewItem(scrapy.Item):
    totalValue       =scrapy.Field()
    circulationValue =scrapy.Field()
    tradValue        =scrapy.Field()
    trunoverRate     =scrapy.Field()
    pushDate         =scrapy.Field()

    def __init__(self,datas,*args,**kw):
        super(SseOverviewItem,self).__init__()
        self._datas           =datas 
        #self.totalValue       =datas['totalValue']
        #self.circulationValue =datas['circulationValue']
        #self.tradValue        =datas['tradValue']
        #self.trunoverRate     =datas['trunoverRate']
        #self.pushDate         =datas['pushDate']

    def convert(self):
        return self._datas
