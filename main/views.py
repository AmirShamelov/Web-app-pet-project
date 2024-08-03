from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    context: dict = {
        "title": "Home - Главная",
        "content": "Магазин мебели Amir Shamelov",
    }

    return render(request, 'main/index.html', context)
def about(request):
    context: dict = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Хорошие товары"
    }

    return render(request, 'main/about.html', context)



