from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomRegistrationForm
from bookings.models import hotelBookings, tourBookings


def user_home(request):
    return render(request, "users/user_home1.html")

def bookings(request):
    userBookings = hotelBookings.objects.filter(user = request.user).order_by('-booked_at')
    userTourBookings = tourBookings.objects.filter(user = request.user).order_by('-booked_at')
    return render(request, "bookings.html", {'userBookings':userBookings, 'tourBookings':userTourBookings})


def sign_up(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("user_home"))
    else:
        form = CustomRegistrationForm()
    return render(request, "registration/sign_up.html", {"form": form})

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login_page')

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('login_page')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('user_home')

    # Render the login page template (GET request)
    return render(request, 'registration/login.html')





