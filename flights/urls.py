from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"), #Param "<int:flight_id>" is required in views.py 'flight()' function
    path("<int:flight_id>/book", views.book, name="book") #Param "<int:flight_id/book>" is required in views.py 'book()' function
]