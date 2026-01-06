from django.urls import include, path
from . import views


urlpatterns = [
    path("user_home/", views.user_home, name="user_home"),
    path("bookings/", views.bookings, name = "bookings"),
    path('login/', views.login_page, name='login_page'),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("accounts/", include("django.contrib.auth.urls")),
]