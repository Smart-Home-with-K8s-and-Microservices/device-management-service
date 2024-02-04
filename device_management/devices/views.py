from rest_framework import viewsets

from .models import Room
from .serializers import RoomSerializer


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer