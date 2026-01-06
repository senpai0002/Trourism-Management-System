from django.urls import include, path
from . import views

urlpatterns = [
    path('bookingConfirmation/', views.bookingConfirmation, name = "booking_Confirmation"),
    path('paymentForm/', views.paymentForm, name = 'payment_form'),
    path('paymentConfirm/', views.paymentConfirm, name = 'payment_confirm'),
    path('tourBookingConfirmation/',views.tourBookingConfirmation, name = "tour_booking_confirmation"),
    path('tourPaymentForm/', views.tourPaymentForm, name = "tour_payment_form"),
    path('tourPaymentConfirm/', views.tourPaymentConfirm, name = "tour_payment_confirm"),
]
