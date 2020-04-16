from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket

def index(request):
    pass

def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # check auth user
    if request.user.is_authenticated:
        basket = request.user.basket.filter(product=product).first()
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
