from django.db import models

# Create your models here.

# class RoomType(models.Model):
#     TYPE_CHOICES = [
#         ('standard', 'standard'),
#         ('deluxe', 'deluxe'),
#         ('premium', 'premium'),
#     ]
#     name = models.CharField(max_length=100, choices=TYPE_CHOICES)

#     def __str__(self):
#         return f"{self.name}"


class room(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    pricePerNight = models.IntegerField(default=1500)
    place = models.CharField(max_length=100, blank=True, default='')
    roomImage = models.ImageField(upload_to = "staticFiles/uploads", null = True, blank = True)
    roomsRemaining = models.IntegerField(null = True)
    Description = models.CharField(max_length = 500, blank = True, default="")

    def __str__(self):
        return f"{self.name}"

    def premium_price(self):
        return self.pricePerNight * 7


    def deluxe_price(self):
        return self.pricePerNight *3



class buses(models.Model):
    bus_types = [
            ('standard', 'Standard'),
            ('ac', 'A/C'),
        ]

    bus_name = models.CharField(max_length = 100, blank = True, default = '')
    des_city = models.CharField(max_length = 100, blank = True, default = '')
    dep_city = models.CharField(max_length = 100, blank = True, default = '')
    price = models.IntegerField()
    bus_type = models.CharField(max_length = 100, choices = bus_types)
    seatsRemaining = models.IntegerField()
    busImage = models.ImageField(upload_to = "staticFiles/uploads/buses", null = True, blank = True)
    Description = models.CharField(max_length = 500, blank = True, default="")

    def __str__(self):
        return f"{self.bus_name}"

class adventures(models.Model):
    name = models.CharField(max_length = 100, blank = True, default = '')
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class tour(models.Model):

    tour_name = models.CharField(max_length = 100, blank = True, default = '')
    city = models.CharField(max_length = 100, blank = True, default = '')
    price = models.IntegerField()
    days = models.IntegerField(null = True)
    nights = models.IntegerField(null = True)
    tourImage = models.ImageField(upload_to = "staticFiles/uploads/tours", null = True, blank = True)
    description = models.CharField(max_length = 500, blank = True, default = "")
    available_adventures = models.ManyToManyField(adventures, blank = True)
    @property
    def nights(self):
        return self.days - 1 if self.days else None

    def __str__(self):
        return f"{self.tour_name}"


class flight(models.Model):
    flight_name = models.CharField(max_length = 100, blank = True, default = '')
    dep_airport = models.CharField(max_length = 100, blank = True, default = '')
    des_airport = models.CharField(max_length = 100, blank = True, default = '')
    image = models.ImageField(upload_to = "staticFiles/uploads/flights", null = True, blank = True)
    description = models.CharField(max_length = 100, blank = True, default = '')
    price = models.IntegerField(null = True)

    def __str__(self):
        return f"{self.flight_name}"