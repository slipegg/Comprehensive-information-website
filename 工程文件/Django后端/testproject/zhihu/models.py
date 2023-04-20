from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

class Z_hot(models.Model):
    Z_hot_list_id=models.AutoField(verbose_name=_('知乎热榜id'),primary_key=True,db_index=True)
    Z_hot_list_time = models.DateTimeField(verbose_name=_('知乎热榜更新时间'), auto_now_add=True)
    Z_hot_list_sum=models.IntegerField (verbose_name=_('知乎热榜查看次数'),default=0)
    # Z_hot_list_url= models.CharField(verbose_name=_('知乎热榜链接'))

class Z_hot_item(models.Model):
    Z_item_id=models.AutoField(verbose_name=_('知乎热榜条目id'),primary_key=True,db_index=True)
    Z_hot_list_id=models.ForeignKey(Z_hot, verbose_name=_('知乎热榜id'), on_delete=models.CASCADE, db_column='Z_hot_list_id', related_name='z_hot')
    Z_item_rank=models.IntegerField (verbose_name=_('知乎热榜条目排名'))
    Z_item_name=models.CharField(verbose_name=_('知乎热榜条目标题'),max_length=500)
    Z_item_hot=models.CharField(verbose_name=_('知乎热榜条目热度值'),max_length=500)
    Z_item_cover_url=models.CharField(verbose_name=_('知乎热榜条目封面图片url'),max_length=500)
    Z_item_click_sum=models.IntegerField (verbose_name=_('知乎热榜条目查看次数'),default=0)
    Z_item_url=models.CharField(verbose_name=_('知乎热榜条目url'),max_length=500)

