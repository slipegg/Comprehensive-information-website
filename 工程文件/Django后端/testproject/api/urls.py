from django.urls import re_path,include,path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # re_path(r'^articles/$', views.article_list),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),
    # # re_path(r'articles', views.ArticleList.as_view()),
    # re_path(r'^articles/$', views.ArticleList.as_view()),
    # # re_path(r'^users/$', views.ArticleList.as_view()),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),
    # re_path(r'^users/$', views.ArticleList.as_view()),
    re_path('register', views.Register.as_view()),
    re_path('login', views.Login.as_view()),
    re_path('chpasswd', views.ChangePasswd.as_view()),
    re_path('chname', views.ChangeName.as_view()),
    re_path('normalUser', views.normalUser.as_view()),
    re_path('superUser', views.superUser.as_view()),
    re_path('isRoot', views.isRoot.as_view()),
    re_path('timeManage',views.crawlTimeManageList.as_view()),
    re_path('rootChangePasswd',views.rootChangePasswd.as_view()),
    # re_path(r'^bili/$', include('bili.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns.append(path('bili/',include('bili.urls')))
urlpatterns.append(path('weibo/',include('weibo.urls')))
urlpatterns.append(path('zhihu/',include('zhihu.urls')))

