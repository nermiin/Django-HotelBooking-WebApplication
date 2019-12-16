from django.contrib import admin

from hotel.models import Room,Roomtype,Roomrate


class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel_hotelid', 'roomid','roomtype_roomtypeid')

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('roomtypeid', 'roomtype')



class RoomrateAdmin(admin.ModelAdmin):
    list_display = ('roomrateid', 'roomtype_roomtypeid')



admin.site.register(Room, RoomAdmin)
admin.site.register(Roomtype, RoomTypeAdmin)
admin.site.register(Roomrate, RoomrateAdmin)
