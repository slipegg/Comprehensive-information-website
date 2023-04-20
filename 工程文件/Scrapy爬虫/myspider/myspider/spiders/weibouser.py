import scrapy
import json
from myspider.items import WeiboUserItem
import datetime
import time
def GMT2stamp(dd):
    GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'
    date_temp = str(datetime.datetime.strptime(dd, GMT_FORMAT))
    # 转换成时间数组
    timeArray = time.strptime(date_temp, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    lasttimestamp = int(time.mktime(timeArray))
    return lasttimestamp
class WeibouserSpider(scrapy.Spider):
    def __init__(self,uid,lasttime):
        self.uid=uid
        self.lasttime=lasttime
        self.start_urls =['https://m.weibo.cn/api/container/getIndex?&containerid='+self.uid]#1076031782488734#1076033708072513

    name = 'weibouser'
    custom_settings = {
        'ITEM_PIPELINES': {'myspider.pipelines.WeiboUserPipeline': 302 },
    }
    def parse(self, response):
        data = (json.loads(response.text))['data']
        # print(type(data),'\n',data)
        # card=data['cards'][1]#['created_at']
        for card in data['cards']:
            post_time=GMT2stamp(card['mblog']['created_at'])
            if int(post_time)<=int(self.lasttime):
                continue
            content=(card['mblog']['text'])
            share=card['mblog']['reposts_count']
            comment=card['mblog']['comments_count']
            like=card['mblog']['attitudes_count']
            wb_id=card['mblog']['mid']
            pic_list=[]
            for i in card['mblog']['pic_ids']:
                pic_list.append('https://wx2.sinaimg.cn/large/'+i)
            user=WeiboUserItem(up_id=self.uid,wb_id=wb_id,content=content,pic_list=json.dumps(pic_list),share=share,comment=comment,like=like,post_time=post_time)
            yield user
