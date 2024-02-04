from django.contrib import admin

from .models import Device, Room, Sensor

# Register your models here.
admin.site.register(Device)
admin.site.register(Sensor)
admin.site.register(Room)
