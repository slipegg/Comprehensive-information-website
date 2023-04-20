from django.contrib import admin
from .models import Z_hot,Z_hot_item
# Register your models here.
class Z_hotAdmin(admin.ModelAdmin):
    list_display = ('Z_hot_list_id', 'Z_hot_list_time', 'Z_hot_list_sum')


    '''10 items per page'''
    list_per_page = 10
class Z_hot_itemAdmin(admin.ModelAdmin):
    list_display = ('Z_item_id', 'Z_hot_list_id', 'Z_item_rank','Z_item_name','Z_item_hot','Z_item_cover_url','Z_item_click_sum','Z_item_url')


    '''10 items per page'''
    list_per_page = 10

admin.site.register(Z_hot,Z_hotAdmin)
admin.site.register(Z_hot_item,Z_hot_itemAdmin)