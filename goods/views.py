from django.shortcuts import render
from goods.models import Products

def catalog(requset):

    goods = Products.objects.all()

    context = {
        'title': 'Home - Каталог',
        'goods': goods,
    }
    return render(requset, "goods/catalog.html", context)


def product(requset):
    return render(requset, "goods/product.html")
