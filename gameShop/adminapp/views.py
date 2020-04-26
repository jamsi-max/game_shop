from django.shortcuts import render
from django.conf import settings

from authapp.models import ShopUser

def index(request):

    content = {
        'page_title': 'admin',
        'user_list': ShopUser.objects.all().order_by('-is_active', '-is_superuser'),
        'mediaURL': settings.MEDIA_URL,

    }
    return render(request, 'adminapp/index.html', context=content)
