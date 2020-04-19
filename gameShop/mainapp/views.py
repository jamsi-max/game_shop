from django.shortcuts import render
import random
from basketapp.models import Basket
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

def get_basket(request):
    return request.user.basket.all() if request.user.is_authenticated else []

def get_same_products(current_product):
    same_products = current_product.category.product_set.exclude(pk=current_product.pk)
    return random.sample(list(same_products), 4) if len(same_products) > 4 else same_products
  

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
        'login_form': ShopUserLoginForm(),
        'basket': get_basket(request), 
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
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
        'login_form': ShopUserLoginForm(),
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/products.html', context=content)


def product(request, pk):
    current_product = current_product = Product.objects.filter(pk=pk).first()
    content = {
        'page_title': 'product',
        'current_product': current_product,
        'products_list': get_same_products(current_product)[:4],
        'login_form': ShopUserLoginForm(),
        'mediaURL': settings.MEDIA_URL,
    }
    return render(request, 'mainapp/product.html', context=content)


def contact(request):
    login_form = ShopUserLoginForm()
    content = {
        'page_title': 'контакты',
        'login_form': login_form,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/contact.html', context=content)
