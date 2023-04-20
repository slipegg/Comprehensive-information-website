import scrapy
from myspider.items import ZhihuItem

class ZhihuSpider(scrapy.Spider):
    def __init__(self,save_index):
        self.save_index=save_index
    custom_settings = {
        'ITEM_PIPELINES':{'myspider.pipelines.ZhihuPipeline': 301}
    }
    name = 'zhihu'
    allowed_domains = ['huashuimoyu.com']
    start_urls = ['http://huashuimoyu.com/detail/3']
    def parse(self, response):
        a_list=response.xpath('(//tbody)[1]//tr')
        for a in a_list:
            rank=a.xpath('./td[1]/text()').extract_first()
            img_url=a.xpath('./td[2]/img/@src').extract_first()
            title=a.xpath('./td[3]/a/text()').extract_first()
            title_url=a.xpath('./td[3]/a/@href').extract_first()
            hot=a.xpath('./td[4]/text()').extract_first()
            zh=ZhihuItem(hot_table_id=self.save_index,rank=rank,img_url=img_url,title=title,title_url=title_url,hot=hot)
            yield zh


