from rest_framework import generics, permissions
from app.models import UniversityFeedback as UniversityFeedbackModel
from app.api.serializers import UniversityFeedback


class UniversityFeedbackListView(generics.ListCreateAPIView):
    queryset = UniversityFeedbackModel.objects.all()
    serializer_class = UniversityFeedback

    permission_classes = [permissions.IsAuthenticated]


class UniversityFeedbackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniversityFeedbackModel.objects.all()
    serializer_class = UniversityFeedback

    permission_classes = [permissions.IsAuthenticated]
