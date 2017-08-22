# * --encoding-- utf8
import requests
from .spiders.cninfo       import CompanyListItem
from .spiders.shiborSpider import ShiborRateItem
from .spiders.sgeSpider    import GlodPriceItem 
from .spiders.sse          import SseOverviewItem
from .spiders.chinaclear   import InvestorOverviewItem

class Agent(object):
    "代理用来对已经爬下来的数据进行处理、如发送到server Agent作为所有其它代理的基类"
    item=None
    server="http://www.cstudio.com/component/"
    api=""
    def __init__(self,item):
        self.item=item

    @property
    def ajaxaddress(self):
        return "{0}{1}".format(self.server,self.api)

    def postToServer(self):
        url=self.ajaxaddress
        requests.post(url,data=self.item.convert())


class ShiborAgent(Agent):
    server="http://www.financedatas.com/component/"
    api="shibor/add"

class CompanyListAgent(Agent):
    server="http://www.financedatas.com/component/"
    api="cninfo/add/company/basicinfo"
    def postToServer(self):
        datas=self.item.convert()
        url=self.ajaxaddress
        for x in datas:
            r=requests.post(url,data={'stockCode':x['stockCode'],
                                    'name'     :x['name'],
                                    'mainPage' :x['infoPage']})
            print(r.text)
        #把url最后一个参数写入本地文件
        arg=datas[0]['infoPage'].split('?')[-1]
        print(arg)
        with open('/tmp/{0}.txt'.format(arg),'w') as f:
            for x in datas:
                f.write("{0}\n".format(x['infoPage'].split('?')[-1]))

class GlodPriceAgent(Agent):
    server="http://www.financedatas.com/component/"
    api="glod/add/"
    def postToServer(self):
        datas=self.item.convert()
        if datas['closing']==-1:
            print('warning closing price equal -1 ...')
            return
        else:
            url=self.ajaxaddress
            r  =requests.post(url,datas)
            print(r.text)

class SseOverViewAgent(Agent):
    server="http://www.financedatas.com/component/"
    api='sse/add/overview'
    def postToServer(self):
        datas=self.item.convert()
        url  =self.ajaxaddress
        r    =requests.post(url,datas)
        print(r.text)

class ChinaClearInvestorOverviewAgent(Agent):
    server="http://www.financedatas.com/component/"
    api="chinaclear/add/investoroverview"
    def postToServer(self):
        datas=self.item.convert()
        print(datas)


def agentRouter(item):
    """
    一个Agent的分发器，不同的的Item分给不同的Agent
    """
    if isinstance(item,ShiborRateItem):
        sa=ShiborAgent(item)
        sa.postToServer()
    
    if isinstance(item,CompanyListItem):
        ci=CompanyListAgent(item)
        ci.postToServer()
    
    if isinstance(item,GlodPriceItem):
        gi=GlodPriceAgent(item)
        gi.postToServer()

    if isinstance(item,SseOverviewItem):
        si=SseOverViewAgent(item)
        si.postToServer()
    
    if isinstance(item,InvestorOverviewItem):
        cci=ChinaClearInvestorOverviewAgent(item)
        cci.postToServer()
