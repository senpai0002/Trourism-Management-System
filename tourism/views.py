from django.shortcuts import render
from django.http import HttpResponse
from .models import room, buses, tour, flight


def home(request):
    if request.user.groups.filter(name = 'HotelAgency').exists():
        return HttpResponse('This is for Hotel Agency')
    else:
        return render(request, 'home1.html')


# Hotel URL
def hotels(request):

    room_type = request.GET.get('hotelType')
    location = request.GET.get('location')
    if room_type and location:
        room_list = room.objects.filter(type = room_type, place = location)
    elif room_type:
        room_list = room.objects.filter(type = room_type)
    elif location:
        location = str(location)
        room_list = room.objects.filter(place__iexact = location)
        # room_list = room.objects.filter(place__icontains = location)
    else:
        room_list = room.objects.all()

    return render(request, 'hotel.html', {"room_list": room_list})


# Travel URL

def travel(request):

    tab_type = request.GET.get('tab_type')
    if tab_type == 'flights':
        active_tab = request.GET.get('tab', 'flights')
    else:
        # Check for tab parameter (default to 'buses')
        active_tab = request.GET.get('tab', 'buses')

    # Get buses with search functionality
    departure_city = request.GET.get('busFrom')
    destination_city = request.GET.get('busTo')

    # Default get all buses
    buses_list = buses.objects.all()

    # Apply filters if search parameters exist
    if departure_city and destination_city:
        buses_list = buses.objects.filter(dep_city__icontains=departure_city, des_city__icontains=destination_city)
    elif departure_city:
        buses_list = buses.objects.filter(dep_city__icontains=departure_city)
    elif destination_city:
        buses_list = buses.objects.filter(des_city__icontains=destination_city)

    # Get flights with search functionality
    departure_airport = request.GET.get('flightFrom')
    destination_airport = request.GET.get('flightTo')
    depart_date = request.GET.get('departDate')

    # Default get all flights
    flights_list = flight.objects.all()

    # Apply filters if search parameters exist
    if departure_airport and destination_airport and depart_date:
        flights_list = flight.objects.filter(
            dep_airport__icontains=departure_airport,
            des_airport__icontains=destination_airport,
            departure_date=depart_date
        )
    elif departure_airport:
        flights_list = flight.objects.filter(dep_airport__icontains=departure_airport)
    elif destination_airport:
        flights_list = flight.objects.filter(des_airport__icontains=destination_airport)
    elif depart_date:
        flights_list = flight.objects.filter(departure_date=depart_date)


    context = {
        'buses_list': buses_list,
        'flights_list': flights_list,
        'active_tab': active_tab,
        'busFrom': departure_city or '',
        'busTo': destination_city or '',
        'flightFrom': departure_airport or '',
        'flightTo': destination_airport or '',
        'departDate': depart_date or '',
    }

    return render(request, 'travelHomePage.html', context)

def tourism(request):
    city = request.GET.get('city')
    tourist_spot = request.GET.get('tour_spot')
    tour_list = None
    # print(city)
    # if (len(city) == 0 and len(tourist_spot) == 0):
    #     tour_list = tour.objects.all()
    # else:

    if city and tourist_spot:
        tour_list = tour.objects.filter(tour_name__icontains = tourist_spot, place__icontains = city)
    elif city:
        tour_list = tour.objects.filter(city__icontains = city)
    elif tourist_spot:
        tour_list = tour.objects.filter(tour_name__icontains = tourist_spot)
    else:
        tour_list = tour.objects.all()
    return render(request, 'tourHomePage.html',{"tour_list": tour_list, "city": city})