from django.shortcuts import render

def login(request):
    context = {
        'title': 'Авторизация'
    }
    return render(
        request=request,
        template_name="users/login.html",
        context=context
    )


def registration(request):
    context = {
        'title': 'Регистрация'
    }
    return render(
        request=request,
        template_name="users/registration.html",
        context=context
    )


def profile(request):
    context = {
        'title': 'Кабинет'
    }
    return render(
        request=request,
        template_name="users/profile.html",
        context=context
    )


def logout(request):
    pass
