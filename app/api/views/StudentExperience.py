from app.models import StudentExperience
from rest_framework.permissions import AllowAnyOrReadOnly
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    StudentExperienceSerializer,
)
from rest_framework import generics, permissions


class StudentExperienceList(ListAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer
    permission_classes = [permissions.AllowAny]


class StudentExperienceCreate(ListCreateAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer

    permission_classes = [permissions.AllowAny]


class StudentExperienceDetail(RetrieveAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer

    permission_classes = [permissions.AllowAny]


class StudentExperienceUpdate(RetrieveUpdateAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer

    permission_classes = [permissions.AllowAny]


class StudentExperienceDelete(RetrieveDestroyAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer

    permission_classes = [permissions.AllowAny]
