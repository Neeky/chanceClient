# * --encoding-- utf8
import requests
from .spiders.cninfo import CompanyListItem
from .spiders.shiborSpider import ShiborRateItem


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



def agentRouter(item):
    """
    一个Agent的分发器，不同的的Item分给不同的Agent
    """
    if isinstance(item,ShiborRateItem):
        sa=ShiborAgent(item)
        sa.postToServer()
