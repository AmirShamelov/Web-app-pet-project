from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

categories = Categories.objects.all()

def index(request):
    context: dict = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        "categories": categories
    }

    return render(request, 'main/index.html', context)
def about(request):
    context: dict = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Хороший товар"
    }

    return render(request, 'main/about.html', context)



