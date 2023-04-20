from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.contrib.auth import settings
User = get_user_model()

# Create your models here.
class Weibo_hot(models.Model):
    Weibo_hot_list_id=models.AutoField(verbose_name=_('微博热门id'),primary_key=True,db_index=True)
    Weibo_hot_list_time = models.DateTimeField(verbose_name=_('微博热门更新时间'), auto_now_add=True)
    Weibo_hot_list_sum=models.IntegerField (verbose_name=_('微博热门查看次数'),default=0)

class Weibo_hot_item(models.Model):
    Weibo_item_id=models.AutoField(verbose_name=_('微博热门条目id'),primary_key=True,db_index=True)
    Weibo_hot_list_id=models.ForeignKey(Weibo_hot, verbose_name=_('微博热门id'), on_delete=models.CASCADE, db_column='Weibo_hot_list_id', related_name='weibo_hot')
    Weibo_item_rank=models.IntegerField (verbose_name=_('微博热门条目排名'))
    Weibo_item_name=models.CharField(verbose_name=_('微博热门条目标题'),max_length=500)
    Weibo_item_hot = models.CharField(verbose_name=_('微博热门条目热度值'), max_length=500,null=True, blank=True)
    Weibo_item_click_sum=models.IntegerField (verbose_name=_('微博热门条目点击次数'),default=0)
    Weibo_item_url=models.CharField(verbose_name=_('微博热门条目url'),max_length=500)

class up_list(models.Model):
    Weibo_up_id=models.CharField (verbose_name=_('微博博主id'),max_length=500,primary_key=True,db_index=True)
    Weibo_up_name=models.CharField(verbose_name=_('微博博主昵称'),max_length=500)
    Weibo_up_face_url=models.CharField(verbose_name=_('微博博主头像url'),max_length=500)
    def __str__(self):
        return self.Weibo_up_name

class follow_list(models.Model):
    Weibo_follow_id = models.AutoField(verbose_name=_('关注列表关系id'), primary_key=True, db_index=True)
    Weibo_up_id=models.ForeignKey(up_list,verbose_name=_('微博博主id'), db_index=True,on_delete=models.CASCADE, db_column='Weibo_up_id', related_name='wbfollow_up_list')
    Weibo_user_id=models.ForeignKey(User, db_index=True,verbose_name=_('本站用户id'),on_delete=models.CASCADE, db_column='Weibo_user_id', related_name='wbfollow_auth_user')
    Weibo_is_special=models.IntegerField(verbose_name=_('是否特别关注'),default=0)

class dynasic_time_list(models.Model):
    up_date_time=models.DateTimeField(verbose_name=_('微博动态更新时间'),primary_key=True,db_index=True)

class dynasic(models.Model):#,null=True, blank=True
    Weibo_dynasic_id=models.AutoField(verbose_name=_('微博动态id'),primary_key=True,db_index=True)
    Weibo_up_id=models.ForeignKey(up_list, verbose_name=_('微博博主id'), on_delete=models.CASCADE, db_column='Weibo_up_id', related_name='Weibo_up_list')
    # Weibo_type=models.IntegerField (verbose_name=_('微博动态类型'))
    Weibo_share=models.IntegerField (verbose_name=_('微博动态分享数'))
    Weibo_comment=models.IntegerField (verbose_name=_('微博动态评论数'))
    Weibo_like=models.IntegerField (verbose_name=_('微博动态点赞数'))
    Weibo_post_time=models.IntegerField (verbose_name=_('微博动态发布时间'))
    Weibo_url_id=models.CharField(verbose_name=_('微博动态链接id'),max_length=500,null=True, blank=True)
    Weibo_content=models.CharField(verbose_name=_('微博动态文字内容'),max_length=5000,null=True, blank=True)
    Weibo_pic_urls=models.CharField(verbose_name=_('微博动态图片链接集合'),max_length=900,null=True, blank=True)
