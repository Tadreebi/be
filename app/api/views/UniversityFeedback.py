from django.forms import ModelForm
from rest_framework import generics, permissions
from app.models import UniversityFeedback
from app.api.serializers import UniversityFeedbackSerializer
from ..permissions import (
    IsOwnerOrReadOnly,
    UniversityPermission,
)


class UniversityFeedbackListView(generics.ListCreateAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    permission_classes = [UniversityPermission, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UniversityFeedbackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    permission_classes = [UniversityPermission, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
