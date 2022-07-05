from app.api.serializers import UniversityFeedbackSerializer
from app.models import UniversityFeedback
from django.forms import ModelForm
from rest_framework import generics, permissions
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
)

from ..permissions import IsOwnerOrReadOnly, UniversityPermission


class UniversityFeedbackList(ListAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer

    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class UniversityFeedbackCreate(ListCreateAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    
    # permission_classes = [UniversityPermission, IsOwnerOrReadOnly]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class UniversityFeedbackDetail(RetrieveAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    
    # permission_classes = [UniversityPermission, IsOwnerOrReadOnly]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class UniversityFeedbackUpdate(RetrieveUpdateAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    
    # permission_classes = [UniversityPermission, IsOwnerOrReadOnly]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class UniversityFeedbackDelete(RetrieveDestroyAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    
    # permission_classes = [UniversityPermission, IsOwnerOrReadOnly]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
