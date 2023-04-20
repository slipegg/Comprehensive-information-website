from django.contrib import admin
from .models import Bili_hot,Bili_hot_item,up_list,dynasic,follow_list
class Bili_hotAdmin(admin.ModelAdmin):
    list_display = ('Bili_hot_list_id', 'Bili_hot_list_time', 'Bili_hot_list_sum')

    '''10 items per page'''
    list_per_page = 10
class Bili_hot_itemAdmin(admin.ModelAdmin):
    list_display = ('Bili_item_id', 'Bili_hot_list_id','Bili_item_name',
                    'Bili_item_up','Bili_item_view','Bili_item_comment','Bili_item_cover_url',
                    'Bili_item_click_sum','Bili_item_url')

    '''10 items per page'''
    list_per_page = 10
class Bili_up_listAdmin(admin.ModelAdmin):
    list_display = ('Bili_up_id', 'Bili_up_name','Bili_up_face_url')

    '''10 items per page'''
    list_per_page = 10
class Bili_dynasicAdmin(admin.ModelAdmin):
    list_display = ('Bili_dynasic_id', 'Bili_up_id','Bili_type','Bili_share','Bili_comment'
                    ,'Bili_like','Bili_post_time','Bili_url_id','Bili_content','Bili_pic_urls',
                    'Bili_video_title','Bili_video_url','Bili_video_pic_url','Bili_video_desc'
                    ,'Bili_original_up','Bili_original_content')

    '''10 items per page'''
    list_per_page = 10

class Bili_follow_listAdmin(admin.ModelAdmin):
    list_display = ('Bili_up_id', 'Bili_user_id','Bili_is_special',)
    '''10 items per page'''
    list_per_page = 10
admin.site.register(Bili_hot, Bili_hotAdmin)
admin.site.register(Bili_hot_item, Bili_hot_itemAdmin)
admin.site.register(up_list, Bili_up_listAdmin)
admin.site.register(dynasic, Bili_dynasicAdmin)
admin.site.register(follow_list, Bili_follow_listAdmin)