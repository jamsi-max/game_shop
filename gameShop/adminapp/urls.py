from django.urls import path, re_path

import adminapp.views as authapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.index, name='index'),
]