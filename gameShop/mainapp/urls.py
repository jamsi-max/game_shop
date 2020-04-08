from django.urls import path, re_path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path('^$', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),
]