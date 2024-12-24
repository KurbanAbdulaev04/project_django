from django.shortcuts import render

# Create your views here.


def platform_start(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'platform.html', context)


def games_shop(request):
    return render(request, 'games.html')


def cart_shop(request):
    return render(request, 'cart.html')
