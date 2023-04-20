from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import settings
User = get_user_model()
# Create your models here.
class Bili_hot(models.Model):
    Bili_hot_list_id=models.AutoField(verbose_name=_('b站热门id'),primary_key=True,db_index=True)
    Bili_hot_list_time = models.DateTimeField(verbose_name=_('b站热门更新时间'), auto_now_add=True)
    Bili_hot_list_sum=models.IntegerField (verbose_name=_('b站热门查看次数'),default=0)

class Bili_hot_item(models.Model):
    Bili_item_id=models.AutoField(verbose_name=_('b站热门视频id'),primary_key=True,db_index=True)
    Bili_hot_list_id=models.ForeignKey(Bili_hot, verbose_name=_('b站热门id'), on_delete=models.CASCADE, db_column='Bili_hot_list_id', related_name='bili_hot')
    Bili_item_name=models.CharField(verbose_name=_('b站热门视频标题'),max_length=500)
    Bili_item_up = models.CharField(verbose_name=_('b站热门视频Up主'), max_length=500)
    Bili_item_view = models.IntegerField(verbose_name=_('b站热门视频观看数'), default=0)
    Bili_item_comment = models.IntegerField(verbose_name=_('b站热门视频评论数'), default=0)
    Bili_item_cover_url=models.CharField(verbose_name=_('b站热门视频封面图片url'),max_length=500)
    Bili_item_click_sum=models.IntegerField (verbose_name=_('b站热门视频点击次数'),default=0)
    Bili_item_url=models.CharField(verbose_name=_('b站热门视频url'),max_length=500)

class up_list(models.Model):
    Bili_up_id=models.IntegerField (verbose_name=_('b站up主id'),primary_key=True,db_index=True)
    Bili_up_name=models.CharField(verbose_name=_('b站up主昵称'),max_length=500)
    Bili_up_face_url=models.CharField(verbose_name=_('b站up主头像url'),max_length=500)
    def __str__(self):
        return self.Bili_up_name

class follow_list(models.Model):#,on_delete=models.CASCADE, db_column='Bili_up_id', related_name='up_list'
    Bili_follow_id = models.AutoField(verbose_name=_('关注列表关系id'), primary_key=True, db_index=True)
    Bili_up_id=models.ForeignKey(up_list,verbose_name=_('b站up主id'), db_index=True,on_delete=models.CASCADE, db_column='Bili_up_id', related_name='follow_up_list')
    Bili_user_id=models.ForeignKey(User, db_index=True,verbose_name=_('本站用户id'),on_delete=models.CASCADE, db_column='Bili_user_id', related_name='follow_auth_user')
    Bili_is_special=models.IntegerField(verbose_name=_('是否特别关注'),default=0)

class dynasic_time_list(models.Model):
    up_date_time=models.DateTimeField(verbose_name=_('b站动态更新时间'),primary_key=True,db_index=True)

class dynasic(models.Model):#,null=True, blank=True
    Bili_dynasic_id=models.AutoField(verbose_name=_('b站动态id'),primary_key=True,db_index=True)
    Bili_up_id=models.ForeignKey(up_list, verbose_name=_('b站up主id'), on_delete=models.CASCADE, db_column='Bili_up_id', related_name='Bili_up_list')
    Bili_type=models.IntegerField (verbose_name=_('b站动态类型'))
    Bili_share=models.IntegerField (verbose_name=_('b站动态分享数'))
    Bili_comment=models.IntegerField (verbose_name=_('b站动态评论数'))
    Bili_like=models.IntegerField (verbose_name=_('b站动态点赞数'))
    Bili_post_time=models.IntegerField (verbose_name=_('b站动态发布时间'))
    Bili_url_id=models.CharField(verbose_name=_('b站动态链接id'),max_length=500,null=True, blank=True)
    Bili_content=models.CharField(verbose_name=_('b站动态文字内容'),max_length=5000,null=True, blank=True)
    Bili_pic_urls=models.CharField(verbose_name=_('b站动态图片链接集合'),max_length=900,null=True, blank=True)
    Bili_video_title=models.CharField(verbose_name=_('b站动态视频标题'),max_length=500,null=True, blank=True)
    Bili_video_url=models.CharField(verbose_name=_('b站动态视频url'),max_length=500,null=True, blank=True)
    Bili_video_pic_url=models.CharField(verbose_name=_('b站动态视频封面url'),max_length=500,null=True, blank=True)
    Bili_video_desc=models.CharField(verbose_name=_('b站动态视频简介'),max_length=1000,null=True, blank=True)
    Bili_original_up = models.CharField(verbose_name=_('b站动态转发的原up'), max_length=1000, null=True, blank=True)
    Bili_original_content=models.CharField(verbose_name=_('b站动态转发的原内容'), max_length=5000, null=True, blank=True)
