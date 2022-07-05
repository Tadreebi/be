from app.models import StudentExperience
from rest_framework.permissions import AllowAny
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

from ..permissions import IsOwnerOrReadOnly, StudentPermission


class StudentExperienceList(ListAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer

    permission_classes = [permissions.AllowAny]


class StudentExperienceCreate(ListCreateAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentExperienceDetail(RetrieveAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentExperienceUpdate(RetrieveUpdateAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentExperienceDelete(RetrieveDestroyAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
