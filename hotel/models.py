# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employee(models.Model):
    employeeid = models.BigAutoField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Guest(models.Model):
    guestid = models.BigAutoField(db_column='GuestID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=45)  # Field name made lowercase.
    birthdate = models.DateField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    employee_employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='Employee_EmployeeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guest'


class Hotel(models.Model):
    hotelid = models.AutoField(db_column='HotelID', primary_key=True)  # Field name made lowercase.
    hotelname = models.TextField(db_column='HotelName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hotel'


class Hotelemployee(models.Model):
    hotel_hotelid = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='Hotel_HotelID', primary_key=True)  # Field name made lowercase.
    employee_employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='Employee_EmployeeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hotelemployee'
        unique_together = (('hotel_hotelid', 'employee_employeeid'),)


class Promo(models.Model):
    promoid = models.BigAutoField(db_column='PromoID', primary_key=True)  # Field name made lowercase.
    promocode = models.CharField(db_column='PromoCode', max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.
    dollardiscount = models.PositiveSmallIntegerField(db_column='DollarDiscount', blank=True, null=True)  # Field name made lowercase.
    percentdiscount = models.PositiveIntegerField(db_column='PercentDiscount', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    roomtype_roomtypeid = models.ForeignKey('Roomtype', models.DO_NOTHING, db_column='RoomType_RoomTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promo'


class Reservation(models.Model):
    reservationid = models.BigAutoField(db_column='ReservationID', primary_key=True)  # Field name made lowercase.
    guest_guestid = models.ForeignKey(Guest, models.DO_NOTHING, db_column='Guest_GuestID')  # Field name made lowercase.
    totalbeforetax = models.DecimalField(db_column='TotalBeforeTax', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservation'


class Reservationdetail(models.Model):
    reservationdetailid = models.BigAutoField(db_column='ReservationDetailID', primary_key=True)  # Field name made lowercase.
    reservation_reservationid = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='Reservation_ReservationID')  # Field name made lowercase.
    roomreservation_roomreservationid = models.ForeignKey('Roomreservation', models.DO_NOTHING, db_column='RoomReservation_RoomReservationID')  # Field name made lowercase.
    roomreservationaddon_roomreservationaddonid = models.BigIntegerField(db_column='RoomReservationAddOn_RoomReservationAddOnID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=12, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservationdetail'


class Reservationpromo(models.Model):
    promo_promoid = models.ForeignKey(Promo, models.DO_NOTHING, db_column='Promo_PromoID', primary_key=True)  # Field name made lowercase.
    reservation_reservationid = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='Reservation_ReservationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservationpromo'
        unique_together = (('promo_promoid', 'reservation_reservationid'),)


class Room(models.Model):
    roomid = models.AutoField(db_column='RoomID', primary_key=True)  # Field name made lowercase.
    roomnumber = models.PositiveSmallIntegerField(db_column='RoomNumber')  # Field name made lowercase.
    floor = models.SmallIntegerField(db_column='Floor')  # Field name made lowercase.
    occupancylimit = models.PositiveSmallIntegerField(db_column='OccupancyLimit')  # Field name made lowercase.
    roomtype_roomtypeid = models.ForeignKey('Roomtype', models.DO_NOTHING, db_column='RoomType_RoomTypeID')  # Field name made lowercase.
    hotel_hotelid = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='Hotel_HotelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'


class Roomrate(models.Model):
    roomrateid = models.BigAutoField(db_column='RoomRateID', primary_key=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=12, decimal_places=2)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    roomtype_roomtypeid = models.ForeignKey('Roomtype', models.DO_NOTHING, db_column='RoomType_RoomTypeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roomrate'


class Roomreservation(models.Model):
    roomreservationid = models.BigAutoField(db_column='RoomReservationID', primary_key=True)  # Field name made lowercase.
    room_roomid = models.ForeignKey(Room, models.DO_NOTHING, db_column='Room_RoomID')  # Field name made lowercase.
    reservation_reservationid = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='Reservation_ReservationID')  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roomreservation'


class Roomreservationguest(models.Model):
    guest_guestid = models.ForeignKey(Guest, models.DO_NOTHING, db_column='Guest_GuestID', primary_key=True)  # Field name made lowercase.
    roomreservation_roomreservationid = models.ForeignKey(Roomreservation, models.DO_NOTHING, db_column='RoomReservation_RoomReservationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roomreservationguest'
        unique_together = (('guest_guestid', 'roomreservation_roomreservationid'),)


class Roomtype(models.Model):
    roomtypeid = models.PositiveSmallIntegerField(db_column='RoomTypeID', primary_key=True)  # Field name made lowercase.
    roomtype = models.CharField(db_column='RoomType', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roomtype'
