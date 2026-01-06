from django.db import models
from django.conf import settings
from tourism.models import room, tour, adventures
from datetime import date, timedelta
# Create your models here.

class hotelBookings(models.Model):
    TYPE_CHOICES = [
        ('standard', 'standard'),
        ('deluxe', 'deluxe'),
        ('premium', 'premium'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'user')
    name = models.CharField(max_length=100, null=True, blank=True)
    hotel = models.ForeignKey(room, on_delete = models.CASCADE, related_name = 'hotel')
    type = models.CharField(max_length=100, null=True, blank=True)
    booked_at = models.DateTimeField(auto_now_add=True)
    checkInDate = models.DateField()
    checkOutDate = models.DateField()
    rent = models.IntegerField(null = True, blank = True)
    totalPayable = models.IntegerField(null = True, blank = True)
    tax = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return f"{self.hotel} booked by ({self.user}) At {self.booked_at.strftime('%Y-%m-%d %H:%M:%S')}"



class tourBookings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'userTour')
    tour = models.ForeignKey(tour, on_delete = models.CASCADE, related_name = 'tour')
    booked_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    bookingDate = models.DateField()
    # bookedFor = models.IntegerField(null = True, blank = True)
    adventures = models.ManyToManyField(adventures, blank = True)
    rent = models.IntegerField(null = True, blank = True)
    totalPayable = models.IntegerField(null = True, blank = True)
    tax = models.IntegerField(null = True, blank = True)


    def __str__(self):
        return f"{self.tour} booked by ({self.user}) At {self.booked_at.strftime('%Y-%m-%d %H:%M:%S')}"
