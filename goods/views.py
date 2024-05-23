from django.shortcuts import render

def catalog(requset):
    return render(requset, "goods/catalog.html")

def product(requset):
    return render(requset, "goods/product.html")