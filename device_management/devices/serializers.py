from rest_framework import serializers

from .models import Device, Room, Sensor


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'name', 'serial', 'model', 'room', 'status')
        read_only_fields = ('serial', 'model', 'status')


class SensorSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)

    class Meta:
        model = Sensor
        depth = 1
        fields = '__all__'
        read_only_fields = ('serial', 'model', 'accepts_commands', 'device')
