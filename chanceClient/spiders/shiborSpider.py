# -*- coding: utf-8 -*-
import scrapy


class ShiborspiderSpider(scrapy.Spider):
    name = 'shiborSpider'
    allowed_domains = ['www.shibor.org']
    start_urls = ['http://www.shibor.org/shibor/web/html/shibor.html#']

    def parse(self, response):
        # 发布时间记录在
        # div 下的第一个table
        # table 下的第一个table(tb2)
        # tb2 这个table的第一个td中的记录
        tb1=response.xpath('//div/descendant::table[position()=1]/descendant::table[position()=1]')
        pushDate=tb1.xpath('.//td[position()=1]/text()').extract_first().strip()
        print(pushDate)

        # 各个期限的利率记录在
        # div 下的第一个table
        # table 下的第三个 table
        tb3=response.xpath('//div/descendant::table[position()=1]/descendant::table[position()=3]')
        # O/N
        oneNight=tb3.xpath('.//tr[position()=1]/td[position()=3]/text()').extract_first().strip()
        # 1W
        oneWeek=tb3.xpath('.//tr[position()=2]/td[position()=3]/text()').extract_first().strip()
        # 2W
        twoWeek=tb3.xpath('.//tr[position()=3]/td[position()=3]/text()').extract_first().strip()
        # 1M
        oneMonth=tb3.xpath('.//tr[position()=4]/td[position()=3]/text()').extract_first().strip()
        # 3M
        threeMonth=tb3.xpath('.//tr[position()=5]/td[position()=3]/text()').extract_first().strip()
        # 6M
        sixMonth=tb3.xpath('.//tr[position()=6]/td[position()=3]/text()').extract_first().strip()
        # 9M
        nineMonth=tb3.xpath('.//tr[position()=7]/td[position()=3]/text()').extract_first().strip()
        # 1Y
        oneYear=tb3.xpath('.//tr[position()=8]/td[position()=3]/text()').extract_first().strip()
        print(oneNight,oneWeek,twoWeek,oneMonth,threeMonth,sixMonth,nineMonth,oneYear)
        pass
