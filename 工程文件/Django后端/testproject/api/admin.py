from django.contrib import admin
from .models import Article,crawlTimeManage


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'create_date')

    '''filter options'''
    list_filter = ('status',)

    '''10 items per page'''
    list_per_page = 10

class crawlTimeManageAdmin(admin.ModelAdmin):
    list_display = ('biliHotTime', 'weiboHotTime', 'zhihuHotTime', 'biliDynasicTime','weiboDynasicTime')

    '''10 items per page'''
    list_per_page = 10

# admin.site.register(Article, ArticleAdmin)
admin.site.register(crawlTimeManage, crawlTimeManageAdmin)