from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>Trailer Bookings</title><h1>Book Alabaster Trailer</h1></html>')