from django.urls import path


from .views import (
    template_view,
    home_view,
    about_us,
    contact_info,
    comment_user,
)

urlpatterns = [
    path('', template_view),
    path('home', home_view, name="home"),
    path('about', about_us, name="about"),
    path('contact_info', contact_info, name="contact_info"),
    path('comment_user', comment_user, name="comment"),
]