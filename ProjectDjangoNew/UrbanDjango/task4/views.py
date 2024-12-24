from django.shortcuts import render

# Create your views here.


def platform_start(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'platform1.html', context)


def games_shop(request):
    title = 'Магазин игр'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'title': title,
        'games': games,
    }
    return render(request, 'games1.html', context)


def cart_shop(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'cart1.html', context)
