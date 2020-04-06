from django.shortcuts import render

# function upload data from file json
import json
import os
def get_data():
    try:
        data = json.load(open(os.path.abspath(r'data.json'), encoding="utf-8"))
    except:
        print("Error load data from BD")
        data = []
    return data

def index(request):
    content = {
        'page_title': 'главная',
        'links_menu': get_data()['links_menu']
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    content = {
        'page_title': 'каталог',
        'links_menu': get_data()['links_menu'],
        'products_list': get_data()['products_list']
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    content = {
        'page_title': 'контакты',
        'links_menu': get_data()['links_menu']
    }
    return render(request, 'mainapp/contact.html', context=content)
