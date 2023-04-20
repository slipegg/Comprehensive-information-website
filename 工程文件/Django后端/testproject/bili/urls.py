from django.urls import re_path,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    re_path(r'^hot_item/$', views.Bili_hot_item_view.as_view()),
    re_path(r'^hot/$', views.Bili_hot_view.as_view()),
    re_path(r'^uplist/$', views.Bili_up_list_view.as_view()),
    re_path(r'^dynasic/$', views.Bili_dynasic_view.as_view()),
    re_path(r'^followlist/$', views.Bili_follow_view.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

