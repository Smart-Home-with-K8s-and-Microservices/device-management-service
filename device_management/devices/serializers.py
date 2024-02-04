from rest_framework import serializers

from .models import Device, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'name', 'serial', 'model', 'room', 'status')
        read_only_fields = ('serial', 'model', 'status')
