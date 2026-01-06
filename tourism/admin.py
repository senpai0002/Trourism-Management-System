from django.contrib import admin
from .models import room, buses, tour, flight, adventures
# Register your models here.

admin.site.register(room)
admin.site.register(buses)
admin.site.register(tour)
admin.site.register(flight)
admin.site.register(adventures)

