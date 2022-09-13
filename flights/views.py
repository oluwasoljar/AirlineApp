from django.http import HttpResponseRedirect
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all() #Grants "flights/index.html" access to all Flights
    }) 

def flight(request, flight_id):
   #flight = Flight.objects.get(id=flight_id) 
   flight = Flight.objects.get(pk=flight_id) #Gets Flight whose i.d. or p.k. is = 'flight_id' (from "flight" path)
   return render(request, "flights/flight.html", { #Render the .html page of the above flight (i.e. "flights/flight.html")
       "flight": flight, #Grants "flights/flight.html" access to flight whose i.d. is = 'flight_id' 
       "passengers": flight.passengers.all(), #Grants "flights/flight.html" access to all passengers on the above flight
       "non_passengers": Passenger.objects.exclude(flights=flight).all()#Grants "flights/flight.html" access to all non passengers
       
   })

def book(request, flight_id):
    if request.method == "POST": #If request method is 'POST' (say Form input submitted)
        flight = Flight.objects.get(pk=flight_id) #Gets Flight whose i.d. or p.k. is = 'flight_id' (from "book" path)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"])) #Gets the passenger whose name is 'POSTED'
        passenger.flights.add(flight) #from all available 'flights', adF passenger to flight '(flight)'

        return HttpResponseRedirect(reverse("flight", args=(flight.id,))) #Return "flights/flight.html" with passenger added 
        #args=(flight.id,) above must be structured as a 'tuple'
