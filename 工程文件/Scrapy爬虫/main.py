from twisted.internet import reactor
from scrapy.crawler import *
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
import os
import datetime
import time
import pymysql
from threading import Thread
cursor=None
def time2stamp(last_time):
    # 转换成时间数组
    timeArray = time.strptime(last_time, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    lasttimestamp = int(time.mktime(timeArray))
    return lasttimestamp
# def bili_spider():
#     ############################b站热榜
#     #'''
#     #查询现在热榜表的最大id
#     sql = 'select * from bili_bili_hot order by Bili_hot_list_id desc limit 1'
#     cursor.execute(sql)
#     res =cursor.fetchall()
#     now_index=0
#     for i in res:
#         now_index=i[0]
#     #插入一行热榜表
#     date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     sql = 'INSERT INTO bili_bili_hot(Bili_hot_list_time,Bili_hot_list_sum) VALUES ("{0}",0)'.format(date_time)
#     cursor.execute(sql)
#     db_connect.commit()
#     #启动爬虫
#     configure_logging()
#     runner = CrawlerRunner(settings=get_project_settings())
#     runner.crawl('bili_hot',now_index+1)
#
#     # '''
#     ########################知乎热榜
#     #'''
#     sql = 'select * from zhihu_z_hot order by Z_hot_list_id desc limit 1'
#     cursor.execute(sql)
#     res =cursor.fetchall()
#     now_index=0
#     for i in res:
#         now_index=i[0]
#     print(now_index)
#     #插入一行热榜表
#     date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     sql = 'INSERT INTO zhihu_z_hot VALUES (null,"{0}",0)'.format(date_time)
#     cursor.execute(sql)
#     db_connect.commit()
#     #启动爬虫
#     # configure_logging()
#     # runner = CrawlerRunner(settings=get_project_settings())
#     runner.crawl('zhihu',now_index+1)
#     #'''
#     ########################微博热榜
#     #'''
#     sql = 'select * from weibo_weibo_hot order by Weibo_hot_list_id desc limit 1'
#     cursor.execute(sql)
#     res =cursor.fetchall()
#     now_index=0
#     for i in res:
#         now_index=i[0]
#     print(now_index)
#     #插入一行热榜表
#     date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     sql = 'INSERT INTO weibo_weibo_hot VALUES (null,"{0}",0)'.format(date_time)
#     cursor.execute(sql)
#     db_connect.commit()
#     #启动爬虫
#     # configure_logging()
#     # runner = CrawlerRunner(settings=get_project_settings())
#     runner.crawl('weibo_hot',now_index+1)
#     #'''
#     #######################b站动态
#     #'''
#     #获得上一次更新的时间
#     sql = 'select * from bili_dynasic_time_list order by up_date_time desc limit 1'
#     cursor.execute(sql)
#     res =cursor.fetchall()
#     last_time=''
#     for i in res:
#         last_time=str(i[0])
#     # last_time='2022-04-28 11:20:22'
#     print(last_time)
#     # 转换成时间数组
#     timeArray = time.strptime(last_time, "%Y-%m-%d %H:%M:%S")
#     # 转换成时间戳
#     lasttimestamp = int(time.mktime(timeArray))
#     print(lasttimestamp)
#     #获得所有需要爬取的uid
#     sql = 'select Bili_up_id from bili_up_list'
#     cursor.execute(sql)
#     res =cursor.fetchall()
#     up_list=[]
#     for i in res:
#         up_list.append(i[0])
#     print(up_list)
#     #启动爬虫
#     # configure_logging()
#     # runner = CrawlerRunner(settings=get_project_settings())
#     for uid in up_list:
#         runner.crawl('up',uid,lasttimestamp)
#
#         #插入一行时间
#     date_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     value=(date_time)
#     sql = 'INSERT INTO bili_dynasic_time_list VALUES (%s)'
#     print(sql,value)
#
#
#     cursor.execute(sql,value)
#     db_connect.commit()
#     #'''
#     #########################微博动态
#     #'''
#     sql = 'select * from weibo_dynasic_time_list order by up_date_time desc limit 1'
#     cursor.execute(sql)
#     res = cursor.fetchall()
#     last_time='2022-04-27 11:20:22'
#     for i in res:
#         last_time = str(i[0])
#     print(last_time)
#     lasttimestamp=time2stamp(last_time)
#     print(lasttimestamp)
#     # 获得所有需要爬取的uid
#     sql = 'select weibo_up_id from weibo_up_list'
#     cursor.execute(sql)
#     res = cursor.fetchall()
#     up_list = []
#     for i in res:
#         up_list.append(i[0])
#     print(up_list)
#     # 启动爬虫
#     # configure_logging()
#     # runner = CrawlerRunner(settings=get_project_settings())
#     for uid in up_list:
#         runner.crawl('weibouser', uid, lasttimestamp)
#
#         # 插入一行时间
#     date_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     value = (date_time)
#     sql = 'INSERT INTO weibo_dynasic_time_list VALUES (%s)'
#     print(sql, value)
#     cursor.execute(sql, value)
#     db_connect.commit()
#     #'''
#     ######################开始爬取
#     deferred = runner.join()
#     deferred.addBoth(lambda _: reactor.stop())
#     reactor.run()

def biliDynasicCraw():
    host = '127.0.0.1'
    port = 3300
    database = 'web'
    user = 'root'
    password = '123456'
    db_connect = pymysql.connect(host=host, port=port, database=database, user=user, password=password,
                                      charset='utf8')
    cursor = db_connect.cursor()
    while(1):
        # 获得上一次更新的时间
        sql = 'select * from bili_dynasic_time_list order by up_date_time desc limit 1'
        cursor.execute(sql)
        res = cursor.fetchall()
        last_time='2022-04-28 11:20:22'
        for i in res:
            last_time = str(i[0])
        print(last_time)
        # 转换成时间数组
        timeArray = time.strptime(last_time, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        lasttimestamp = int(time.mktime(timeArray))
        print(lasttimestamp)
        # 获得所有需要爬取的uid
        sql = 'select Bili_up_id from bili_up_list'
        cursor.execute(sql)
        res = cursor.fetchall()
        up_list = []
        for i in res:
            up_list.append(i[0])
        print(up_list)
        # 启动爬虫
        # configure_logging()
        # runner = CrawlerRunner(settings=get_project_settings())
        for uid in up_list:
            # print('4')
            os.system("scrapy crawl up -a uid=" + str(uid) + " -a lasttime=" + str(lasttimestamp))
        # 插入一行时间
        date_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        value = (date_time)
        sql = 'INSERT INTO bili_dynasic_time_list VALUES (%s)'
        cursor.execute(sql, value)
        db_connect.commit()
        time.sleep(getSleepTime(4))

def weiboDynasicCraw():
    host = '127.0.0.1'
    port = 3300
    database = 'web'
    user = 'root'
    password = '123456'
    db_connect = pymysql.connect(host=host, port=port, database=database, user=user, password=password,
                                      charset='utf8')
    cursor = db_connect.cursor()
    while(1):
        sql = 'select * from weibo_dynasic_time_list order by up_date_time desc limit 1'
        cursor.execute(sql)
        res = cursor.fetchall()
        last_time = '2022-04-27 11:20:22'
        for i in res:
            last_time = str(i[0])
        print(last_time)
        lasttimestamp = time2stamp(last_time)
        print(lasttimestamp)
        # 获得所有需要爬取的uid
        sql = 'select weibo_up_id from weibo_up_list'
        cursor.execute(sql)
        res = cursor.fetchall()
        up_list = []
        for i in res:
            up_list.append(i[0])
        print(up_list)
        # 启动爬虫
        for uid in up_list:
            # print('5')
            os.system("scrapy crawl weibouser -a uid=" + str(uid)+" -a lasttime="+str(lasttimestamp))
            # runner.crawl('weibouser', uid, lasttimestamp)
        # 插入一行时间
        date_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        value = (date_time)
        sql = 'INSERT INTO weibo_dynasic_time_list VALUES (%s)'
        print(sql, value)
        cursor.execute(sql, value)
        db_connect.commit()
        time.sleep(getSleepTime(5))
def weiboHotCraw():
    host = '127.0.0.1'
    port = 3300
    database = 'web'
    user = 'root'
    password = '123456'
    db_connect = pymysql.connect(host=host, port=port, database=database, user=user, password=password,
                                      charset='utf8')
    cursor = db_connect.cursor()
    while(1):
        sql = 'select * from weibo_weibo_hot order by Weibo_hot_list_id desc limit 1'
        cursor.execute(sql)
        res = cursor.fetchall()
        now_index = 0
        for i in res:
            now_index = i[0]
        print(now_index)
        # 插入一行热榜表
        date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = 'INSERT INTO weibo_weibo_hot VALUES (null,"{0}",0)'.format(date_time)
        cursor.execute(sql)
        db_connect.commit()
        # 启动爬虫
        os.system("scrapy crawl weibo_hot -a save_index=" + str(now_index + 1))
        time.sleep(getSleepTime(2))

def biliHotCraw():
    ############################b站热榜
    # '''
    # 查询现在热榜表的最大id
    host = '127.0.0.1'
    port = 3300
    database = 'web'
    user = 'root'
    password = '123456'
    db_connect = pymysql.connect(host=host, port=port, database=database, user=user, password=password,
                                      charset='utf8')
    cursor = db_connect.cursor()
    while(1):
        sql = 'select * from bili_bili_hot order by Bili_hot_list_id desc limit 1'
        cursor.execute(sql)
        res = cursor.fetchall()
        now_index = 0
        for i in res:
            now_index = i[0]
        # 插入一行热榜表
        date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = 'INSERT INTO bili_bili_hot(Bili_hot_list_time,Bili_hot_list_sum) VALUES ("{0}",0)'.format(date_time)
        cursor.execute(sql)
        db_connect.commit()
        # 启动爬虫
        os.system("scrapy crawl bili_hot -a save_index=" + str(now_index + 1))
        time.sleep(getSleepTime(1))

def zhihuHotCraw():
    host = '127.0.0.1'
    port = 3300
    database = 'web'
    user = 'root'
    password = '123456'
    db_connect = pymysql.connect(host=host, port=port, database=database, user=user, password=password,
                                      charset='utf8')
    cursor = db_connect.cursor()
    while(1):
        sql = 'select * from zhihu_z_hot order by Z_hot_list_id desc limit 1'
        cursor.execute(sql)
        res = cursor.fetchall()
        now_index = 0
        for i in res:
            now_index = i[0]
        print(now_index)
        # 插入一行热榜表
        date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = 'INSERT INTO zhihu_z_hot VALUES (null,"{0}",0)'.format(date_time)
        cursor.execute(sql)
        db_connect.commit()
        # 启动爬虫
        os.system("scrapy crawl zhihu -a save_index="+str(now_index + 1))
        time.sleep(getSleepTime(3))


def GMT2stamp(dd):
    GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'
    date_temp = str(datetime.datetime.strptime(dd, GMT_FORMAT))
    # 转换成时间数组
    timeArray = time.strptime(date_temp, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    lasttimestamp = int(time.mktime(timeArray))
    return lasttimestamp

def getSleepTime(index):
    host = '127.0.0.1'
    port = 3300
    database = 'web'
    user = 'root'
    password = '123456'
    db_connect = pymysql.connect(host=host, port=port, database=database, user=user, password=password,
                                      charset='utf8')
    cursor = db_connect.cursor()
    # biliHotTime = t[1]
    # weiboHotTime = t[2]
    # zhihuHotTime = t[3]
    # biliDynasicTime = t[4]
    # weiboDynasicTime = t[5]
    sql = 'select * from api_crawltimemanage where id=1'
    cursor.execute(sql)
    res = cursor.fetchall()
    t= None
    for i in res:
        t = i
    return int(t[index])*60

if __name__=="__main__":
    os.chdir('./myspider/myspider')

    t1 = Thread(target=biliDynasicCraw, args=())
    t1.start()
    t2 = Thread(target=weiboDynasicCraw, args=())
    t2.start()
    t3 = Thread(target=biliHotCraw, args=())
    t3.start()
    t4 = Thread(target=weiboHotCraw, args=())
    t4.start()
    t5 = Thread(target=zhihuHotCraw, args=())
    t5.start()
    # weiboDynasicCraw()
    # zhihuHotCraw()
    # biliHotCraw()
    # weiboHotCraw()

    # global cursor
    #

    # bili_spider()
    # while(1):
    #     zhihuHotCraw()
    #     time.sleep(5)
    # biliHotCraw()
    # while True:
    #     # bili_spider()
    #     try:
    #         biliHotCraw()
    #         time.sleep(3)
    #         print("已经爬取",n,"次")
    #     except:
    #         time.sleep(3)
    #         continue