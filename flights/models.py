from django.db import models

# Create your models here.

#MODEL THAT DEFINES 'Airports'
# Displays Airport 'code & city' (using 'def __str__(self):')
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"

 
 #MODEL THAT DEFINES 'Flights'
 # Displays Flight 'origin, destination & duration' (using 'def __str__(self):')
 # Has access to Flight's Airport info (code & city for origin / code & city for destination)
 # Gives 'Airport' model's objects access to Flight info (origin, destination & duration) via 'related_name' fields. 
    # e.g. in shell we can say:
     #  lhr = Airport(code="LHR", city="London")  
     #  lhr.save()

     #  jfk = Airport(code="JFK", city="New York")  
     #  jfk.save()

     #  f = Flight(origin=jfk, destination=lhr, duration=415)
     #  f.save()

     #  lhr.arrivals.all()      :- means show all flights arriving 'LHR Airport in London'
     #  OUTPUT :- <Flight: 3: New York (JFK) to London (LHR). Duration is 415 mins.>

    # 'lhr' here is an 'Airport object' while 'arrivals' is a 'related_name' 
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        #return f"{self.id}: {self.origin} to {self.destination}. Duration is {self.duration} mins."
        return f"{self.id}: {self.origin} to {self.destination}."

#MODEL THAT DEFINES 'Passengers'
# Displays Passenger's first and last name (using 'def __str__(self):')
# Has access to Passenger's Flight info (origin (code & city), destination (code & city) & duration of flight(s)) 
# Gives 'Flight' model's objects access to Passenger info (first & last) via 'related_name' field    
   # e.g. in shell we can say:
    #   jfk = Airport(code="JFK", city="New York")  
    #   jfk.save()
    #   lhr = Airport(code="LHR", city="London")  
    #   lhr.save()
    #   f = Flight(origin=jfk, destination=lhr, duration=415)
    #   f.save()

    #   f.passengers.all()        :- means show all passengers in Flight 'f' (i.e. 'New York-JFK' to 'London-LHR')  
    #   OUTPUT :- <QuerySet []>   :- means no passenger has been added to Flight 'f'

    #   passenger = Passenger(first="Tom", last="Redlov")
    #   passenger.save()

    #   passenger.flights.add(f) :- means add flight 'f' to the passenger's set of 'flights'

    #   f.passengers.all()        :- means show all passengers in Flight 'f' (i.e. 'New York-JFK' to 'London-LHR')
    #   OUTPUT :- <QuerySet [<Passenger: Tom Redlov>]>  :- means 1 passenger (Tom Redlov) has been added to Flight 'f'

   # 'f' here is a 'Flight object' while 'passengers' is a 'related_name' 

# Has 'Many to Many' relationship with Flight model
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers") 

    def __str__(self):
        return f"{self.first} {self.last}"