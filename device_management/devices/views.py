from rest_framework import viewsets

from .models import Device, Room, Sensor
from .serializers import DeviceSerializer, RoomSerializer, SensorSerializer


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'put', 'patch']

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class SensorViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'put', 'patch']

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
