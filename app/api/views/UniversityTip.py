from app.api.serializers import UniversityTipsSerializer
from app.models import UniversityTip
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework import generics, permissions


class UniversityTipsList(ListAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipsCreate(ListCreateAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipsDetail(RetrieveAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipsUpdate(RetrieveUpdateAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipsDelete(RetrieveDestroyAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.IsAuthenticated]
