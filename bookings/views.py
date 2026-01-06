from django.shortcuts import render
from .models import hotelBookings, tourBookings
from tourism.models import room, tour
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages


# def user_orders(request):
#     orders = hotelBookings.objects.filters(user = request.user)
#     return render(request, 'booking.html', {'orders': orders})


@login_required
def bookingConfirmation(request):
    hotel = get_object_or_404(room, pk = int(request.POST.get('hotel_id')))  # Fetch Room object
    if request.method == "POST":
        context = {

                "hotel_id": hotel.id,
                "hotel_name": hotel.name,
                "hotel_desc": hotel.Description,
                "hotel_rent": hotel.pricePerNight,
                "hotel_place": hotel.place,
                "hotel_image": hotel.roomImage.url if hotel.roomImage else None,
                # "hotel_type": ", ".join([t.name for t in hotel.type.all()]),  # Get all room types
                "premium_price": hotel.premium_price(),  # Call the function
                "deluxe_price": hotel.deluxe_price(),
            }
    return render(request, 'HotelBookingForm.html', context)

# hotel Payment Form
def paymentForm(request):
    if request.method == "POST":
        context = {
            "checkInDate":request.POST.get('checkInDate'),
            "checkOutDate":request.POST.get('checkOutDate'),
            "hotel_id": request.POST.get('hotel_id'),
            "hotel_rent" : request.POST.get('totalHotelRent'),
            "taxes" : request.POST.get('taxesInput'),
            "totalAmount": request.POST.get('totalAmountInput'),
            "hotelType" : request.POST.get('hotelType')
        }
        return render(request, 'paymentForm.html', context)

# create hotel Booking
def paymentConfirm(request):
    if request.method == "POST":

        date_format = '%Y-%m-%d'
        hotel_id = request.POST.get('hotel_id')
        checkInDate = request.POST.get('checkInDate')
        checkOutDate = request.POST.get('checkOutDate')
        datetime.strptime(checkInDate, date_format)
        datetime.strptime(checkOutDate, date_format)
        hotel = room.objects.get(id=hotel_id)
        # days = (checkOutDate-checkInDate)
        hotel_rent = request.POST.get('hotel_rent')
        hotelType = request.POST.get('hotelType')
        totalPay = request.POST.get('totalAmount')
        tax = request.POST.get('taxes')
        obj = room.objects.get(pk = hotel_id)
        # if obj.roomsRemaining > 0:
        obj.roomsRemaining = obj.roomsRemaining - 1
        name = request.POST.get('card-name')
        hotelBookings.objects.create(user = request.user,name = name, hotel = hotel,type = hotelType , checkInDate = checkInDate, checkOutDate = checkOutDate, rent = hotel_rent, totalPayable = totalPay, tax = tax)
        obj.save()
        messages.success(request, f"Your booking for {obj.name} hotel has been confirmed successfully!")
        return redirect('user_home')

@login_required
def tourBookingConfirmation(request):
    if request.method == "POST":
        Tour = get_object_or_404(tour, pk = int(request.POST.get('tour_id')))

        context = {
            "tour_id": Tour.id,
            "tour_name": Tour.tour_name,
            "tour_price": Tour.price,
            "tour_city": Tour.city,
            "tour_image":Tour.tourImage,
            "tour_duration": Tour.days,
            "tour_desciption": Tour.description,
        }

    return render(request, 'tourBookingForm.html', context)

def tourPaymentForm(request):
    if request.method == "POST":
        Tour = get_object_or_404(tour, pk = int(request.POST.get('tour_id')))
        context = {
            "startDate": request.POST.get('startDate'),
            "tour_id": Tour.id,
            "tour_name": Tour.tour_name,
            "tour_price": Tour.price,
            "tour_taxes": round(int(Tour.price)*0.18),
            "tour_totalAmount": int(Tour.price)+ round(int(Tour.price)*0.18),
            "tour_city": Tour.city,
            "tour_image":Tour.tourImage,
            "tour_duration": Tour.days,
            "tour_desciption": Tour.description,
            "tour_adventures": Tour.available_adventures,
        }
        return render(request, 'tourPaymentForm.html',context)


def tourPaymentConfirm(request):
    if request.method == "POST":
        Tour = get_object_or_404(tour, pk = int(request.POST.get('tour_id')))
        date_format = '%Y-%m-%d'
        # context = {
        #     "tour_id": Tour.id,
        #     "tour_name": Tour.tour_name,
        #     "tour_price": Tour.price,
        #     "tour_city": Tour.city,
        #     "startDate": request.POST.get('startDate'),
        #     "tour_image":Tour.tourImage,
        #     "tour_duration": Tour.days,
        #     "tour_desciption": Tour.description,
        # }
        startDate = request.POST.get('startDate')
        datetime.strptime(startDate, date_format)
        tax = round(int(Tour.price)*0.18)
        name = request.POST.get('card-name')
        tourBookings.objects.create(user = request.user, tour = Tour,name = name, rent = Tour.price, bookingDate = startDate, totalPayable = Tour.price + tax, tax = tax)
        messages.success(request, f"Your booking for {Tour.tour_name} tour has been confirmed successfully!")
        return redirect('user_home')






# @login_required
# def bookHotel(request):
# def createBooking(request):
#     hotelBookings.objects.create(user =
#     return