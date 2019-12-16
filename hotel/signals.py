from django.dispatch import Signal
from django.db.models.signals import post_save

from hotel.models import Room


def saveRoom(sender, instance, **kwargs):
    print("Request finished!")


post_save.connect(saveRoom, sender=Room)
