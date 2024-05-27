from django.shortcuts import render
from goods.models import Products

def catalog(requset):

    goods = Products.objects.all()

    context = {
        'title': 'Home - Каталог',
        'goods': goods,
    }
    return render(requset, "goods/catalog.html", context)


def product(requset, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(requset, "goods/product.html", context)
