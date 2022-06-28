from app.models import ComapnyRating
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    ComapnyRatingSerializer,
)
from rest_framework import generics, permissions


class ComapnyRatingList(ListAPIView):
    queryset = ComapnyRating.objects.all()
    serializer_class = ComapnyRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComapnyRatingCreate(ListCreateAPIView):
    queryset = ComapnyRating.objects.all()
    serializer_class = ComapnyRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComapnyRatingDetail(RetrieveAPIView):
    queryset = ComapnyRating.objects.all()
    serializer_class = ComapnyRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComapnyRatingUpdate(RetrieveUpdateAPIView):
    queryset = ComapnyRating.objects.all()
    serializer_class = ComapnyRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComapnyRatingDelete(RetrieveDestroyAPIView):
    queryset = ComapnyRating.objects.all()
    serializer_class = ComapnyRatingSerializer
    permission_classes = [permissions.IsAuthenticated]
