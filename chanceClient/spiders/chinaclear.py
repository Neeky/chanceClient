import scrapy
from   datetime import datetime

now    =datetime.now()

class InvestorOverviewItem(scrapy.Item):
    newlyAddInvestors=scrapy.Field()
    endInvestors     =scrapy.Field()
    pushDate         =scrapy.Field()

    def convert(self):
        datas=dict(self)
        res  ={}
        assert len(datas['newlyAddInvestors']) ==1,'exception in InvestorOverviewItem.convert len != 1'
        assert len(datas['endInvestors'])      ==1,'exception in InvestorOverviewItem.convert len != 1'
        newlyAddInvestors =datas['newlyAddInvestors'][0].replace(',','')
        endInvestors      =datas['endInvestors'][0].replace(',','')
        res['newlyAddInvestors']=float(newlyAddInvestors)
        res['endInvestors']     =float(endInvestors)
        res['pushDate']         ='{0:0>#4}-{1:0>#2}-{2:0>#2}'.format(now.year,now.month,now.day)
        return res
