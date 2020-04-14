from django.urls import path, re_path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    re_path('^login/$', authapp.login, name='login'),
    path('logout/<str:page>/', authapp.logout, name='logout'),
    re_path('^reg/$', authapp.reg, name='reg'),
    re_path('^edit/$', authapp.edit, name='edit'),
]