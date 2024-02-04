from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (DeviceViewSet, FlashSerialDevice, GetSerialDevice,
                    RoomsViewSet, SensorViewSet)

router = DefaultRouter()
router.register(r'rooms', RoomsViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'sensors', SensorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('flash/<int:id>', FlashSerialDevice.as_view(), name='flash'),
    path('serial/', GetSerialDevice.as_view(), name='serial'),
]
