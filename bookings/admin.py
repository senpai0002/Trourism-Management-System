from django.contrib import admin
from .models import hotelBookings, tourBookings
# Register your models here.

admin.site.register(hotelBookings)
admin.site.register(tourBookings)