# -*- coding: utf-8 -*-
import scrapy
from   scrapy.loader import ItemLoader
from   .chinaclear   import InvestorOverviewItem 

class ChinaclearinvestoroverviewSpider(scrapy.Spider):
    name = 'chinaClearInvestorOverview'
    allowed_domains = ['www.chinaclear.cn']
    start_urls = ['http://www.chinaclear.cn/cms-search/view.action?action=china&viewType=&dateStr=&channelIdStr=']

    def parse(self, response):
       tb="//div[@id='settlementList']/table[position()=1]//table[position()=1]"
       ccil=ItemLoader(item=InvestorOverviewItem(),response=response)
       ccil.add_xpath('newlyAddInvestors',"string("+
                                          tb+"//tr[position()=2]/td[position()=2]/p/span/text())")
       ccil.add_xpath('endInvestors'     ,"string("+
                                          tb+"//tr[position()=5]/td[position()=2]/p/span/text())") 
       return ccil.load_item() 
