from django.shortcuts import render
from django.http import HttpResponse
from .form import UserRegister

# Create your views here.


def sign_up_by_html(request):
    users = ['Nikita', 'Andrey']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        print(username)
        print(password)
        print(repeat_password)
        print(age)
        print()

        if password == repeat_password and age >= 18 and not username in users:
            return HttpResponse(f'Приветствуем, {username}!')

        elif username in users:
            info['error'] = 'Пользователь уже существует'

        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'

    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    users = ['Nikita', 'Andrey']
    context = {
        'form': '',
        'error': ''
    }

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['passwprd']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

        if password == repeat_password and age >= 18 and not username in users:
            return HttpResponse(f'Приветствуем, {username}!')

        elif username in users:
            context['error'] = 'Пользователь уже существует'

        elif password != repeat_password:
            context['error'] = 'Пароли не совпадают'

        elif age < 18:
            context['error'] = 'Вы должны быть старше 18'

    else:
        form = UserRegister()
    context['form'] = form

    return render(request, 'registration_page.html', context)
