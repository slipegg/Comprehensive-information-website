import scrapy
import json
from myspider.items import DynamicItem


class UpSpider(scrapy.Spider):
    def __init__(self,uid,lasttime):
        self.uid=uid
        self.lasttime=lasttime
        self.start_urls = ['https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid='+str(uid)]#嘉然：672328094 可汗：23947287

    name = 'up'
    allowed_domains = ['bilibili.com']
    custom_settings = {
        'ITEM_PIPELINES': {'myspider.pipelines.BilibiliUserPipeline': 400 },
    }
    def parse(self, response):
        data = json.loads(response.text)
        cards=data['data']['cards']
        i=0
        for card in cards:
            post_time=card['desc']['timestamp']
            if int(post_time)<=int(self.lasttime):
                continue
            i+=1
            bili_id=card['desc']['dynamic_id_str']
            try:
                temp=json.loads(card['card'])
                share=temp['stat']['share']
                comment=temp['stat']['reply']
                like=temp['stat']['like']
            except:
                share=card['desc']['repost']
                comment=card['desc']['comment']
                like=card['desc']['like']
            if card['desc']['type']==4:#自己发动态
                card = card['card']
                jcard = json.loads(card)
                content=jcard['item']['content']
                Item=DynamicItem(bili_id=bili_id,type=0,share=share,comment=comment,like=like,post_time=post_time,
                                 content=content,up_id=self.uid)
                yield Item
            elif card['desc']['orig_type']==8:#转发视频
                card = card['card']
                jcard = json.loads(card)
                jjcard=json.loads(jcard['origin'])
                share_comm=jcard['item']['content']
                title=jjcard['title']
                desc=jjcard['desc']
                owner=jjcard['owner']['name']
                pic_url=jjcard['pic']
                video_url=jjcard['short_link']
                Item = DynamicItem(bili_id=bili_id,type=4, share=share, comment=comment, like=like, post_time=post_time,
                                   content=share_comm,video_title=title, video_url=video_url, video_pic_url=pic_url,
                                   video_desc=desc,original_up=owner,up_id=self.uid)
                yield Item
            elif card['desc']['orig_type']==2:#转发的动态
                tcard=card['card']
                jcard = json.loads(tcard)
                share_comm = jcard['item']['content']
                content = json.loads(jcard['origin'])['item']['description']
                owner=json.loads(jcard['origin'])['user']['name']
                Item = DynamicItem(bili_id=bili_id,type=3, share=share, comment=comment, like=like, post_time=post_time,
                                   content=share_comm,original_up=owner,original_content=content,up_id=self.uid)
                yield Item
            elif card['desc']['type']==8 and card['desc']['orig_type']==0:#自己发布视频
                card=card['card']
                jcard=json.loads(card)
                video_title=jcard['title']
                video_url=jcard['short_link']
                pic_url=jcard['pic']
                desc=str(jcard['desc']).replace('\n','')
                content=jcard['dynamic']
                Item=DynamicItem(bili_id=bili_id,type=2,share=share,comment=comment,like=like,post_time=post_time,
                                video_title=video_title,video_url=video_url,video_pic_url=pic_url,
                                 video_desc=desc,up_id=self.uid,content=content)
                yield Item
            elif card['desc']['type']==2 and card['desc']['orig_type']==0:#自己发布的带图片的动态
                card = card['card']
                jcard = json.loads(card)
                content = jcard['item']['description']
                pic_url_list=jcard['item']['pictures']
                pic_urls=[]
                for p in pic_url_list:
                    pic_urls.append(p['img_src'])
                Item=DynamicItem(bili_id=bili_id,type=1,share=share,comment=comment,like=like,post_time=post_time,
                                 content=content,pic_urls=json.dumps(pic_urls),up_id=self.uid)
                yield Item
