from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()
class crawlTimeManage(models.Model):
    biliHotTime=models.IntegerField (verbose_name=_('b站热门刷新时间/min'),default=1)
    weiboHotTime=models.IntegerField (verbose_name=_('微博热门刷新时间/min'),default=1)
    zhihuHotTime=models.IntegerField (verbose_name=_('知乎热门刷新时间/min'),default=1)
    biliDynasicTime=models.IntegerField (verbose_name=_('b站动态刷新时间/min'),default=1)
    weiboDynasicTime=models.IntegerField (verbose_name=_('微博动态刷新时间/min'),default=1)

class Article(models.Model):
    """Article Model"""
    STATUS_CHOICES = (
        ('p', _('Published')),
        ('d', _('Draft')),
    )

    title = models.CharField(verbose_name=_('Title (*)'), max_length=90, db_index=True)
    body = models.TextField(verbose_name=_('Body'), blank=True)
    author = models.ForeignKey(User, verbose_name=_('Author'), on_delete=models.CASCADE, related_name='articles')
    status = models.CharField(_('Status (*)'), max_length=1, choices=STATUS_CHOICES, default='s', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
        verbose_name = "Article"
        verbose_name_plural = "Articles"

