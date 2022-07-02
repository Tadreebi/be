from app.models import CompanyRating
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    CompanyRatingSerializer,
)
from rest_framework import generics, permissions


class CompanyRatingList(ListAPIView):
    queryset = CompanyRating.objects.all()
    serializer_class =CompanyRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyRatingCreate(ListCreateAPIView):
    queryset = CompanyRating.objects.all()
    serializer_class =CompanyRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyRatingDetail(RetrieveAPIView):
    queryset = CompanyRating.objects.all()
    serializer_class =CompanyRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyRatingUpdate(RetrieveUpdateAPIView):
    queryset = CompanyRating.objects.all()
    serializer_class =CompanyRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyRatingDelete(RetrieveDestroyAPIView):
    queryset = CompanyRating.objects.all()
    serializer_class =CompanyRatingSerializer
    permission_classes = [permissions.IsAuthenticated]
