from django.shortcuts import render

# function upload data from file json
import json
import os
def get_data():
    try:
        data = json.load(open(os.path.abspath(r'gameShop\data.json'), encoding="utf-8"))
    except:
        print('Error load data from BD')
        data = []
    return data

LINKS_MENU = [
    {'name': 'home', 'href':'index'},
    {'name': 'gallery','href':'products'},
    {'name': 'Contact Us', 'href':'contact'}
]

def index(request):
    data = get_data()
    print(data)
    content = {
        'page_title': 'главная',
        'links_menu': LINKS_MENU
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    content = {
        'page_title': 'каталог',
        'links_menu': LINKS_MENU
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    content = {
        'page_title': 'контакты',
        'links_menu': LINKS_MENU
    }
    return render(request, 'mainapp/contact.html', context=content)
