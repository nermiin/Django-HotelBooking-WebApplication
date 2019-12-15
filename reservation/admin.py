from django.contrib import admin

# Register your models here.
from django.contrib import admin

from hotel.models import Reservation,Reservationdetail

admin.site.register(Reservation)
admin.site.register(Reservationdetail)
