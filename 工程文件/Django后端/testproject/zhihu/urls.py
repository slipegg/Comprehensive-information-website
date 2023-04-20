from django.urls import re_path,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    re_path(r'^hot_item/$', views.Z_hot_item_view.as_view()),
    re_path(r'^hot/$', views.Z_hot_view.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

