from django.shortcuts import render
import random

from mainapp.models import ProductCategory, Product, MainSocial, Services, News, Team
from django.conf import settings

from authapp.forms import ShopUserLoginForm

# function upload data from file json
# !!! ONLY UTF-8 decode
# import json
# import os
# def get_data():
#     try:
#         with open(os.path.abspath('data.json'), 'r', encoding="utf-8") as file:
#             data = json.load(file)
#     except:
#         print("Error load data from BD")
#         data = []
#     return data


def index(request):
    print()
    if request.method != 'POST':
        login_form = ShopUserLoginForm()
    services = Services.objects.all()
    products_list = Product.objects.all()
    main_social = MainSocial.objects.all()
    news = News.objects.order_by('-data')[:3]
    team = Team.objects.all()[:4]
    content = {
        'page_title': 'главная',
        'social_links': main_social,
        'products_list': random.sample(list(products_list), 4),
        'services': services,
        'news': news,
        'team': team,
        'mediaURL': settings.MEDIA_URL,
        'login_form': login_form, 
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
    if request.method != 'POST':
        login_form = ShopUserLoginForm()
    if pk is not None and pk != 0:
        products_list = Product.objects.filter(category__pk=pk)
    else:
        products_list = Product.objects.all()
    category = ProductCategory.objects.all()
    content = {
        'page_title': 'каталог',
        'products_list': products_list,
        'category': category,
        'mediaURL': settings.MEDIA_URL,
        'login_form': login_form,
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    if request.method != 'POST':
        login_form = ShopUserLoginForm()
    content = {
        'page_title': 'контакты',
        'login_form': login_form,
    }
    return render(request, 'mainapp/contact.html', context=content)
