# -*- coding: utf-8 -*-
import scrapy
from .sse import SseOverviewItem


class SseoverviewspiderSpider(scrapy.Spider):
    name = 'sseOverviewSpider'
    allowed_domains = ['www.sse.com.cn']
    start_urls = ['http://www.sse.com.cn/market/stockdata/overview/day/']

    def parse(self, response):
        script    = response.xpath("//table/descendant::script/text()").extract_first().split('\n')
        variables = [v.strip().replace('var','') for v in script if 'var' in v]
        variables = [(v.split('=')[0].strip(),
                      v.split('=')[1].strip().replace(';','').replace("'",'')) for v in variables]
        variables =dict(variables)
        res       ={}
        res['totalValue']       =float(variables['marketValueA'])
        res['circulationValue'] =float(variables['negotiableValueA'])
        res['tradValue']        =float(variables['trdAmtA'])
        res['turnoverRate']     =res['tradValue']/res['totalValue']
        res['PERate']           =float(variables['profitRateA'])
        res['pushDate']         =variables['searchDate']
        return SseOverviewItem(datas=res)
