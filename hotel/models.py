# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Hotel(models.Model):
    hotelid = models.IntegerField(db_column='HotelID', primary_key=True)  # Field name made lowercase.
    hotelname = models.CharField(db_column='HotelName', max_length=20, blank=True,
                                 null=True)
    hotelimage=models.ImageField(upload_to='images/')



    class Meta:
        managed = False
        db_table = 'hotel'


class Employee(models.Model):
    employeeid = models.BigIntegerField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=45, blank=True,
                                 null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Guest(models.Model):
    guestid = models.BigIntegerField(db_column='GuestID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=45, blank=True,
                                 null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    employee_employeeid = models.BigIntegerField(db_column='Employee_EmployeeID', blank=True,
                                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guest'


class Hotelemployee(models.Model):
    hotel_hotelid = models.IntegerField(db_column='Hotel_HotelID', blank=True, null=True)  # Field name made lowercase.
    employee_employeeid = models.BigIntegerField(db_column='Employee_EmployeeID', blank=True,
                                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hotelemployee'


class Promo(models.Model):
    promoid = models.BigIntegerField(db_column='PromoID', primary_key=True)  # Field name made lowercase.
    promocode = models.CharField(db_column='PromoCode', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45, blank=True,
                                   null=True)  # Field name made lowercase.
    roomtype_roomtypeid = models.SmallIntegerField(db_column='RoomType_RoomTypeID', blank=True,
                                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promo'


class Reservation(models.Model):
    reservationid = models.BigIntegerField(db_column='ReservationID', primary_key=True)  # Field name made lowercase.
    guest_guestid = models.BigIntegerField(db_column='Guest_GuestID', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservation'


class Reservationdetail(models.Model):
    reservationdetailid = models.BigIntegerField(db_column='ReservationDetailID',
                                                 primary_key=True)  # Field name made lowercase.
    reservation_reservationid = models.BigIntegerField(db_column='Reservation_ReservationID', blank=True,
                                                       null=True)  # Field name made lowercase.
    roomreservation_roomreservationid = models.BigIntegerField(db_column='RoomReservation_RoomReservationID',
                                                               blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservationdetail'


class Reservationpromo(models.Model):
    promo_promoid = models.BigIntegerField(db_column='Promo_PromoID', blank=True,
                                           null=True)  # Field name made lowercase.
    reservation_reservationid = models.BigIntegerField(db_column='Reservation_ReservationID', blank=True,
                                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservationpromo'


class Room(models.Model):
    roomid = models.IntegerField(db_column='RoomID', primary_key=True)  # Field name made lowercase.
    roomtype_roomtypeid = models.SmallIntegerField(db_column='RoomType_RoomTypeID', blank=True,
                                                   null=True)  # Field name made lowercase.
    hotel_hotelid = models.IntegerField(db_column='Hotel_HotelID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'


class Roomrate(models.Model):
    roomrateid = models.BigIntegerField(db_column='RoomRateID', primary_key=True)  # Field name made lowercase.
    roomtype_roomtypeid = models.SmallIntegerField(db_column='RoomType_RoomTypeID', blank=True,
                                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roomrate'


class Roomreservation(models.Model):
    roomreservationid = models.BigIntegerField(db_column='RoomReservationID',
                                               primary_key=True)  # Field name made lowercase.
    room_roomid = models.IntegerField(db_column='Room_RoomID', blank=True, null=True)  # Field name made lowercase.
    reservation_reservationid = models.BigIntegerField(db_column='Reservation_ReservationID', blank=True,
                                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roomreservation'


class Roomreservationguest(models.Model):
    guest_guestid = models.BigIntegerField(db_column='Guest_GuestID', blank=True,
                                           null=True)  # Field name made lowercase.
    roomreservation_roomreservationid = models.BigIntegerField(db_column='RoomReservation_RoomReservationID',
                                                               blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roomreservationguest'


class Roomtype(models.Model):
    roomtypeid = models.SmallIntegerField(db_column='RoomTypeID', primary_key=True)  # Field name made lowercase.
    roomtype = models.CharField(db_column='RoomType', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roomtype'
