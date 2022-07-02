from rest_framework import generics, permissions
from app.models import UniversityFeedback
from app.api.serializers import UniversityFeedbackSerializer


class UniversityFeedbackListView(generics.ListCreateAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityFeedbackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]
