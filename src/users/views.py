from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(
                username=username,
                password=password
            )
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
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
