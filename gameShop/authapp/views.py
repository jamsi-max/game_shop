from django.shortcuts import render, HttpResponseRedirect, reverse
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.urls import reverse
from django.conf import settings

def login(request):

    login_form = ShopUserLoginForm(data=request.POST)
    print(f'1 - {login_form.errors}')
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
    
        user = auth.authenticate(username=username, password=password)
        
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def reg(request):

    if request.method == 'POST':
        reg_form = ShopUserRegisterForm(request.POST, request.FILES)

        if reg_form.is_valid():
            reg_form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        reg_form = ShopUserRegisterForm()

    content={
        'page_title': 'registration',
        'reg_form': reg_form,
    }
    return render(request, 'authapp/reg.html', context=content)


def edit(request):

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
    
    content = {
        'page_title': 'edit',
        'edit_form': edit_form,
        'mediaURL': settings.MEDIA_URL,
    }

    return render(request, 'authapp/edit.html', context=content)