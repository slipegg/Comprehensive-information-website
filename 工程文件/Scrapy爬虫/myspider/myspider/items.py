# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    hot_table_id = scrapy.Field()
    title = scrapy.Field()
    pic_url = scrapy.Field()
    desc = scrapy.Field()
    up = scrapy.Field()
    video_url = scrapy.Field()
    view = scrapy.Field()
    danmu = scrapy.Field()

class DynamicItem(scrapy.Item):
    up_id=scrapy.Field()
    type = scrapy.Field()#类型0自己发布的动态1自己发布带图片2自己发布的视频3转发的动态4转发的视频
    share = scrapy.Field()
    comment = scrapy.Field()
    like = scrapy.Field()
    post_time = scrapy.Field()
    # up_name = scrapy.Field()
    # up_face_url=scrapy.Field()
    bili_id=scrapy.Field()

    content = scrapy.Field()#文字内容
    pic_urls = scrapy.Field()#图片

    video_title = scrapy.Field()#视频标题
    video_url = scrapy.Field()#视频链接
    video_pic_url = scrapy.Field()#视频封面
    video_desc = scrapy.Field()#视频简介

    original_up = scrapy.Field()#转发的原up
    original_content = scrapy.Field()#转发的原内容

class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    hot_table_id = scrapy.Field()
    rank = scrapy.Field()
    img_url = scrapy.Field()
    title = scrapy.Field()
    title_url = scrapy.Field()
    hot = scrapy.Field()
class WeiboItem(scrapy.Item):
    hot_table_id = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    title_url = scrapy.Field()
    hot = scrapy.Field()

class WeiboUserItem(scrapy.Item):
    # name=scrapy.Field()
    # face_url=scrapy.Field()
    up_id = scrapy.Field()
    content = scrapy.Field()
    share = scrapy.Field()
    comment = scrapy.Field()
    like = scrapy.Field()
    post_time = scrapy.Field()
    pic_list = scrapy.Field()
    wb_id=scrapy.Field()
