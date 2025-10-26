from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    return render(
        request=request,
        template_name="home.html"
    )


def about_us(request):
    return render(
        request=request,
        template_name="about.html"
    )


def contact_info(request):
    return render(
        request=request,
        template_name="contact_info.html"
    )


def comment_user(request):
    return render(
        request=request,
        template_name="comment_user.html"
    )