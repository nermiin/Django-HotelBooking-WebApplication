# Register your models here.
from django.contrib import admin

from hotel.models import Reservation,Guest, Reservationdetail, Roomreservation, Roomreservationguest,Reservationpromo


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservationid', 'guest_guestid')


class GuestAdmin(admin.ModelAdmin):
    list_display = ('guestid', 'firstname','lastname','employee_employeeid')

class ReservationdetailAdmin(admin.ModelAdmin):
    list_display = ('reservation_reservationid','reservationdetailid','roomreservation_roomreservationid','description')


class RoomreservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_reservationid', 'room_roomid','roomreservationid')



class RoomreservationguestAdmin(admin.ModelAdmin):
    list_display = ('guest_guestid', 'roomreservation_roomreservationid')

class ReservationpromoAdmin(admin.ModelAdmin):
    list_display = ('promo_promoid', 'reservation_reservationid')


admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Guest,GuestAdmin)
admin.site.register(Reservationdetail,ReservationdetailAdmin)
admin.site.register(Roomreservation,RoomreservationAdmin)
admin.site.register(Roomreservationguest,RoomreservationguestAdmin)
admin.site.register(Reservationpromo,ReservationpromoAdmin)
