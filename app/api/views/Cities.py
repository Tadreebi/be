from app.models import Cities
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    CitiesSerializer,
)
from rest_framework import generics, permissions


class CitiesList(ListAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    
    permission_classes = [permissions.AllowAny]


class CitiesCreate(ListCreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


class CitiesDetail(RetrieveAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


class CitiesUpdate(RetrieveUpdateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


class CitiesDelete(RetrieveDestroyAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
