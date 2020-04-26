from django.shortcuts import render

def index(request):
    content = {
        'page_title': 'admin',

    }
    return render(request, 'adminapp/index.html', context=content)
