from django.shortcuts import render
import random

from mainapp.models import ProductCategory, Product, MainSocial, Services, News, Team
from django.conf import settings

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
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
    print(pk)
    products_list = Product.objects.all()
    content = {
        'page_title': 'каталог',
        'products_list': random.sample(list(products_list), 4),
        'category': products_list,
        'mediaURL': settings.MEDIA_URL,
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    content = {
        'page_title': 'контакты',
    }
    return render(request, 'mainapp/contact.html', context=content)
