# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
'''
class BilibiliHotPipeline:
    def open_spider(self, spider):
        print('+++++++++++++++++++')
        print(spider.name)
        self.fp = open('up-dynasic.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        dic={}
        print('-------------')
        for i in item:
            dic[i]=item[i]
        self.fp.write(str(dic))
        return item

    def close_spider(self, spider):
        self.fp.close()
'''
from itemadapter import ItemAdapter
import pymysql
import datetime

class BilibiliHotPipeline:
    def open_spider(self, spider):
        host = spider.settings.get('MYSQL_HOST')
        port = spider.settings.get('MYSQL_PORT')
        database = spider.settings.get('MYSQL_DATABASE')
        user = spider.settings.get('MYSQL_USER')
        password = spider.settings.get('MYSQL_PASSWORD')
        self.db_connect = pymysql.connect(host=host, port=port, database=database, user=user, password=password, charset='utf8')
        self.cursor = self.db_connect.cursor()
    def process_item(self, item, spider):
        self.insert_db(item)
        return item
    def close_spider(self, spider):
        self.db_connect.commit()
        self.db_connect.close()
    def insert_db(self, item):
        hot_value=(item['title'],item['up'],item['view'],item['danmu'],item['pic_url'],0,item['video_url'],item['hot_table_id'])
        sql = 'INSERT INTO bili_bili_hot_item VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s)'
        print(sql, hot_value)
        self.cursor.execute(sql, hot_value)

class BilibiliUserPipeline:
    def open_spider(self, spider):
        host = spider.settings.get('MYSQL_HOST')
        port = spider.settings.get('MYSQL_PORT')
        database = spider.settings.get('MYSQL_DATABASE')
        user = spider.settings.get('MYSQL_USER')
        password = spider.settings.get('MYSQL_PASSWORD')
        self.db_connect = pymysql.connect(host=host, port=port, database=database, user=user, password=password, charset='utf8')
        self.cursor = self.db_connect.cursor()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def close_spider(self, spider):
        self.db_connect.commit()
        self.db_connect.close()

    def insert_db(self, item):
        print(item.keys())
        all_key=item.keys()
        need_key=['type','share','comment','like','post_time','bili_id','content','pic_urls','video_title'
                 ,'video_url','video_pic_url','video_desc','original_up','original_content','up_id']
        # str_key=['bili_id','content','pic_urls','video_title'
        #          ,'video_url','video_pic_url','video_desc','original_up','original_content']
        value=[]
        for k in need_key:
            if k in all_key:
                value.append(item[k])
            else:
                value.append('null')
        print(value)
        print('+++++++++++++')
        tv=(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7]
            ,value[8],value[9],value[10],value[11],value[12],value[13],value[14])

        sql = 'INSERT INTO bili_dynasic VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # print(sql,tv)
        # value=(item['type'],item['share'],item['comment'],item['like'],item['post_time'],item['bili_id']
        #            ,item['content'],item['pic_urls'],item['video_title'],item['video_url']
        #            ,item['video_pic_url'],item['video_desc'],item['original_up']
        #            ,item['original_content'],item['up_id'])
        # sql = 'INSERT INTO zhihu_z_hot_item VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        print(sql,tv)
        self.cursor.execute(sql, tv)
        print("数据保存成功！")

class ZhihuPipeline:
    def open_spider(self, spider):
        host = spider.settings.get('MYSQL_HOST')
        port = spider.settings.get('MYSQL_PORT')
        database = spider.settings.get('MYSQL_DATABASE')
        user = spider.settings.get('MYSQL_USER')
        password = spider.settings.get('MYSQL_PASSWORD')
        self.db_connect = pymysql.connect(host=host, port=port, database=database, user=user, password=password, charset='utf8')
        self.cursor = self.db_connect.cursor()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def close_spider(self, spider):
        self.db_connect.commit()
        self.db_connect.close()

    def insert_db(self, item):
        hot_value=(item['rank'],item['title'],item['hot'],item['img_url'],0,item['title_url'],item['hot_table_id'])
        sql = 'INSERT INTO zhihu_z_hot_item VALUES (null,%s,%s,%s,%s,%s,%s,%s)'
        print(sql, hot_value)
        self.cursor.execute(sql, hot_value)

class WeiboPipeline:
    def open_spider(self, spider):
        host = spider.settings.get('MYSQL_HOST')
        port = spider.settings.get('MYSQL_PORT')
        database = spider.settings.get('MYSQL_DATABASE')
        user = spider.settings.get('MYSQL_USER')
        password = spider.settings.get('MYSQL_PASSWORD')
        self.db_connect = pymysql.connect(host=host, port=port, database=database, user=user, password=password, charset='utf8')
        self.cursor = self.db_connect.cursor()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def close_spider(self, spider):
        self.db_connect.commit()
        self.db_connect.close()

    def insert_db(self, item):
        hot_value=(item['rank'],item['title'],item['hot'],0,item['title_url'],item['hot_table_id'])
        sql = 'INSERT INTO weibo_weibo_hot_item VALUES (null,%s,%s,%s,%s,%s,%s)'
        print(sql, hot_value)
        self.cursor.execute(sql, hot_value)

class WeiboUserPipeline:
    def open_spider(self, spider):
        host = spider.settings.get('MYSQL_HOST')
        port = spider.settings.get('MYSQL_PORT')
        database = spider.settings.get('MYSQL_DATABASE')
        user = spider.settings.get('MYSQL_USER')
        password = spider.settings.get('MYSQL_PASSWORD')
        self.db_connect = pymysql.connect(host=host, port=port, database=database, user=user, password=password, charset='utf8mb4')
        self.cursor = self.db_connect.cursor()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def close_spider(self, spider):
        self.db_connect.commit()
        self.db_connect.close()

    def insert_db(self, item):
        print(item.keys())
        all_key=item.keys()
        need_key=['share','comment','like','post_time','wb_id','content',
                  'pic_list','up_id']
        # str_key=['bili_id','content','pic_urls','video_title'
        #          ,'video_url','video_pic_url','video_desc','original_up','original_content']
        value=[]
        for k in need_key:
            if k in all_key:
                value.append(item[k])
            else:
                value.append('null')
        print(value)
        print('+++++++++++++')
        tv=(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7])

        sql = 'INSERT INTO weibo_dynasic VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s)'
        # print(sql,tv)
        # value=(item['type'],item['share'],item['comment'],item['like'],item['post_time'],item['bili_id']
        #            ,item['content'],item['pic_urls'],item['video_title'],item['video_url']
        #            ,item['video_pic_url'],item['video_desc'],item['original_up']
        #            ,item['original_content'],item['up_id'])
        # sql = 'INSERT INTO zhihu_z_hot_item VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        print(sql,tv)
        self.cursor.execute(sql, tv)
        print("数据保存成功！")