from django.contrib import admin

# Register your models here.

from .models import Hotel, Hotelemployee, Employee, Promo


class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotelname', 'hotelid')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employeeid', 'firstname', 'lastname')


class HotelemployeeAdmin(admin.ModelAdmin):
    list_display = ('hotel_hotelid', 'employee_employeeid')


class PromoAdmin(admin.ModelAdmin):
    list_display = ('promoid', 'promocode', 'description', 'roomtype_roomtypeid')


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Hotelemployee, HotelemployeeAdmin)
admin.site.register(Promo, PromoAdmin)

