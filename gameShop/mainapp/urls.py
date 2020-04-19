from django.urls import path, re_path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.products, name='index'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('<int:pk>/', mainapp.product, name='product'),
]