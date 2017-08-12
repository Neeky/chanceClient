# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .spiders.cninfo import CompanyListItem
from .spiders.shiborSpider import ShiborRateItem 
from .agent import agentRouter

class ChanceclientPipeline(object):
    def process_item(self, item, spider):
        print('--'*24)
        print(item.convert())
        #print(isinstance(item,CompanyListItem))
        print('--'*24)
        agentRouter(item)
        return item
