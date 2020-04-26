from django.urls import path, re_path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.index, name='index'),

    re_path(r'^category/$', adminapp.category, name='category'),

    re_path(r'^product/(?P<pk>\d+)/$', adminapp.product, name='product'),
    
    re_path(r'^news/$', adminapp.news, name='news'),
    re_path(r'^news/add/$', adminapp.news_add, name='news_add'),
    re_path(r'^news/update/(?P<pk>\d+)/$', adminapp.news_update, name='news_update'),
    re_path(r'^news/delete/(?P<pk>\d+)/$', adminapp.news_delete, name='news_delete'),
]