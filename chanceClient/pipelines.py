# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ChanceclientPipeline(object):
    def process_item(self, item, spider):
        print('......'*10)
        print(item.convert())
        print('......'*10)
        return item
