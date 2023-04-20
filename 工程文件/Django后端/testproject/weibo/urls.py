from django.urls import re_path,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    re_path(r'^hot_item/$', views.Weibo_hot_item_view.as_view()),
    re_path(r'^hot/$', views.Weibo_hot_view.as_view()),
    re_path(r'^uplist/$', views.Weibo_up_list_view.as_view()),
    re_path(r'^dynasic/$', views.Weibo_dynasic_view.as_view()),
    re_path(r'^followlist/$', views.Weibo_follow_view.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

