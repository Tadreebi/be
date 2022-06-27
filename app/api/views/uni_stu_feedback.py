from rest_framework import generics, permissions
from app.models import UniStuFeedback as UniStuFeedbackModel
from app.api.serializers import UniStuFeedback


class UniStuFeedbackListView(generics.ListCreateAPIView):
    queryset = UniStuFeedbackModel.objects.all()
    serializer_class = UniStuFeedback
    permission_classes = [permissions.IsAuthenticated]


class UniStuFeedbackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniStuFeedbackModel.objects.all()
    serializer_class = UniStuFeedback
    permission_classes = [permissions.IsAuthenticated]
