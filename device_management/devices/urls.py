from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DeviceViewSet, RoomsViewSet

router = DefaultRouter()
router.register(r'rooms', RoomsViewSet)
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
