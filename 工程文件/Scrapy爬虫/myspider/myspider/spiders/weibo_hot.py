import scrapy
import json
from myspider.items import WeiboItem
class WbSpider(scrapy.Spider):
    def __init__(self,save_index):
        self.save_index=save_index
    name = 'weibo_hot'
    allowed_domains = ['huashuimoyu.com']
    start_urls = ['http://huashuimoyu.com/detail/2']
    custom_settings = {
        'ITEM_PIPELINES':{'myspider.pipelines.WeiboPipeline': 302}
    }
    def parse(self, response):
        a_list=response.xpath('(//tbody)[1]//tr')
        for a in a_list:
            rank=a.xpath('./td[1]/text()').extract_first()
            title=a.xpath('./td[2]/a/text()').extract_first()
            title_url=a.xpath('./td[2]/a/@href').extract_first()
            hot=a.xpath('./td[3]/text()').extract_first()
            # print(rank)
            zh=WeiboItem(hot_table_id=self.save_index,rank=rank,title=title,title_url=title_url,hot=hot)
            yield zh
