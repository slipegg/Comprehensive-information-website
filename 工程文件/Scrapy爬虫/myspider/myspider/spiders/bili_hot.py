import scrapy
import json
import time
import pymysql
from myspider.items import BilibiliItem
class BiliHotSpider(scrapy.Spider):
    def __init__(self,save_index):
        self.save_index=save_index
    name = 'bili_hot'
    allowed_domains = ['api.bilibili.com']
    start_urls = ['https://api.bilibili.com/x/web-interface/popular?pn=1']
    custom_settings = {
        'ITEM_PIPELINES': {'myspider.pipelines.BilibiliHotPipeline': 300},
    }
    page=1
    def parse(self, response):
        # while(1):
            text=response.text
            stext=json.loads(text)
            for t in stext['data']['list']:
                title=t['title']
                pic_url=t['pic']
                desc=t['desc']
                up=t['owner']['name']
                video_url=t['short_link']
                view=t['stat']['view']
                danmu=t['stat']['danmaku']
                bi = BilibiliItem(hot_table_id=self.save_index,title=title,pic_url=pic_url,up=up,video_url=video_url,view=view,danmu=danmu,desc=desc)
                yield bi
            if self.page<3:
                self.page+=1
                url='https://api.bilibili.com/x/web-interface/popular?pn='+str(self.page)
                yield scrapy.Request(url=url, callback=self.parse)
            # time.sleep(3)