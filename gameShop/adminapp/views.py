from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product, News
from adminapp.forms import AdminNewsAddForm


@user_passes_test(lambda x: x.is_superuser)
def index(request):

    content = {
        'page_title': 'admin',
        'user_list': ShopUser.objects.all().order_by('-is_active', '-is_superuser'),
        'mediaURL': settings.MEDIA_URL,
    }
    return render(request, 'adminapp/index.html', context=content)


@user_passes_test(lambda x: x.is_superuser)
def category(request):

    content = {
        'page_title': 'admin',
        'category_list': ProductCategory.objects.all().order_by('id'),
    }
    return render(request, 'adminapp/category_list.html', context=content)


@user_passes_test(lambda x: x.is_superuser)
def product(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    content = {
        'page_title': 'admin',
        'category': category,
        'product_list': category.product_set.all().order_by('-price'),
        'mediaURL': settings.MEDIA_URL,
    }
    return render(request, 'adminapp/product_list.html', context=content)


@user_passes_test(lambda x: x.is_superuser)
def news(request):

    content = {
        'page_title': 'admin',
        'news': News.objects.all().order_by('-is_active', '-data',),
    }
    return render(request, 'adminapp/news.html', context=content)


@user_passes_test(lambda x: x.is_superuser)
def news_add(request):

    if request.method == 'POST':
        form = AdminNewsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:news'))
    else:
        form = AdminNewsAddForm()

    content = {
        'page_title': 'admin: news add',
        'form': form,
    }
    return render(request, 'adminapp/news_add.html', context=content)


@user_passes_test(lambda x: x.is_superuser)
def news_update(request, pk):
    
    news = get_object_or_404(News, pk=pk)

    if request.method == 'POST':
        form = AdminNewsAddForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:news'))
    else:
        form = AdminNewsAddForm(instance=news)

    content = {
        'page_title': 'admin: news update',
        'form': form,
    }
    return render(request, 'adminapp/news_add.html', context=content)


@user_passes_test(lambda x: x.is_superuser)
def news_delete(request, pk):

    if request.method == 'POST':
        news = get_object_or_404(News, pk=pk)
        if news.is_active:
            news.is_active = False
            news.save()
            return HttpResponseRedirect(reverse('admin:news'))
        else:
            news.is_active = True
            news.save()
            return HttpResponseRedirect(reverse('admin:news'))
    else:
        form = AdminNewsAddForm()

    content = {
        'page_title': 'admin: news delete',
        'news': get_object_or_404(News, pk=pk),
    }
    return render(request, 'adminapp/news_delete.html', context=content)