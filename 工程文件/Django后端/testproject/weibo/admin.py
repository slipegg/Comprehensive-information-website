from django.contrib import admin
from .models import Weibo_hot,Weibo_hot_item,up_list,dynasic,follow_list

class Weibo_hotAdmin(admin.ModelAdmin):
    list_display = ('Weibo_hot_list_id', 'Weibo_hot_list_time', 'Weibo_hot_list_sum')

    '''10 items per page'''
    list_per_page = 10
class Weibo_hot_itemAdmin(admin.ModelAdmin):
    list_display = ('Weibo_item_id', 'Weibo_hot_list_id', 'Weibo_item_rank','Weibo_item_name',
                    'Weibo_item_click_sum','Weibo_item_url')

    '''10 items per page'''
    list_per_page = 10

class Weibo_up_listAdmin(admin.ModelAdmin):
    list_display = ('Weibo_up_id', 'Weibo_up_name','Weibo_up_face_url')

    '''10 items per page'''
    list_per_page = 10
class Weibo_dynasicAdmin(admin.ModelAdmin):
    list_display = ('Weibo_dynasic_id', 'Weibo_up_id','Weibo_share','Weibo_comment'
                    ,'Weibo_like','Weibo_post_time','Weibo_url_id','Weibo_content','Weibo_pic_urls',
                    )

    '''10 items per page'''
    list_per_page = 10

class Weibo_follow_listAdmin(admin.ModelAdmin):
    list_display = ('Weibo_up_id', 'Weibo_user_id','Weibo_is_special',)
    '''10 items per page'''
    list_per_page = 10
admin.site.register(Weibo_hot, Weibo_hotAdmin)
admin.site.register(Weibo_hot_item, Weibo_hot_itemAdmin)
admin.site.register(up_list, Weibo_up_listAdmin)
admin.site.register(dynasic, Weibo_dynasicAdmin)
admin.site.register(follow_list, Weibo_follow_listAdmin)