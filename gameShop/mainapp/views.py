from django.shortcuts import render
import random

# function upload data from file json
# import json
# import os
# def get_data():
#     try:
#         with open(os.path.abspath(r'data.json'), 'r', encoding="utf-8") as file:
#             data = json.load(file)
#     except:
#         print("Error load data from BD")
#         data = []
#     return data


def index(request):
    data = get_data()
    content = {
        'page_title': 'главная',
        'links_menu': data['links_menu'],
        'social_links':  data['main_social'],
        'products_list': random.sample(data['products_list'], 4),
        'services': data['services'],
        'news': data['news'],
        'team': data['team']
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    data = get_data()
    content = {
        'page_title': 'каталог',
        'links_menu': data['links_menu'],
        'products_list': data['products_list']
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    data = get_data()
    content = {
        'page_title': 'контакты',
        'links_menu': data['links_menu']
    }
    return render(request, 'mainapp/contact.html', context=content)
