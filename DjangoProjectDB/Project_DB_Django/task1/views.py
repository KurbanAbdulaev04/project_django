from django.shortcuts import render
from django.http import HttpResponse
from .form import UserRegister
from .models import Buyer, Game, News
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def platform_start(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/platform1.html', context)


def games_shop(request):
    title = 'Магазин игр'
    games = Game.objects.all()
    context = {
        'title': title,
        'games': games,
    }
    return render(request, 'fourth_task/games1.html', context)


def cart_shop(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'fourth_task/cart1.html', context)


def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        users = Buyer.objects.values_list('name', flat=True)

        if username in users:
            info['error'] = 'Пользователь уже существует'

        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'

        else:
            Buyer.objects.create(name=username, age=age, balance=1000)
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    form = UserRegister(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            age = form.cleaned_data['age']

            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')

            users = Buyer.objects.values_list('name', flat=True)

            if username in users:
                info['error'] = 'Пользователь уже существует'

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

            else:
                Buyer.objects.create(name=username, age=age, balance=1000)
                return HttpResponse(f'Приветствуем, {username}!')

        info['form'] = form

    return render(request, 'fifth_task/registration_page.html', info)


def news(request):
    posts = News.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        news = paginator.get_page(page_number)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'second_task/news.html', {'news': news})
