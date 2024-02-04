from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Device, Room, Sensor
from .serializers import (DeviceSerializer, FlashSerialDeviceSerializer,
                          RoomSerializer, SensorSerializer)
from .utils import compile_and_flash_device


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


class FlashSerialDevice(APIView):
    '''API endpoint for flashing an Arduino device over a serial connection.'''

    def post(self, request, id):

        serializer = FlashSerialDeviceSerializer(data=request.data)

        if serializer.is_valid():

            try:
                # Retrieve the Device instance based on the provided id
                device_instance = Device.objects.get(pk=id)

                # Extract validated data from the serializer
                validated_data = serializer.validated_data
                ssid_name = validated_data.get('ssid_name', {})
                ssid_password = validated_data.get('ssid_password', {})
                ip_address = validated_data.get('ip_address', {})

                # Get necessary information for compilation and flash process from the Device instance
                fqbn = device_instance.fqbn
                sketch_name = device_instance.sketch_name

                # Call the utility function to compile and flash the device
                compile_and_flash_device(ssid_name,
                                         ssid_password,
                                         ip_address,
                                         fqbn,
                                         sketch_name)

                # Return success response
                return Response({'success': f'Device {device_instance.serial} was flashed successfuly.'})

            except Device.DoesNotExist:
                # Handle the case where the device is not found
                return Response({'error': f'Device with ID {id} not found.'})

            except Exception as e:
                # Handle other exceptions and return error response
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # If validation fails, return the DRF validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
