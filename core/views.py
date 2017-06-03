from django.shortcuts import render
from core.models import Product
from django.http import Http404


def almaty(request, *args, **kwargs):
    p = Product.objects.order_by('-price')
    return render(request, 'core/almaty.html', {
        'products': p,
    })


def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'core/detail.html', {'products': product})
