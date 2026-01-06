from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hotels/", views.hotels, name = "hotels"),
    path("travel/", views.travel, name = "travel"),
    path("tourism/", views.tourism, name = "tour"),
    # path("flight_search/", views.flight_search, name = "flight_search"),
]