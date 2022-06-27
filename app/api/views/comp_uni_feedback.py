from rest_framework import generics, permissions
from app.models import CompUniFeedback as CompUniFeedbackModel
from app.api.serializers import CompUniFeedback


class CompUniFeedbackListView(generics.ListCreateAPIView):
    queryset = CompUniFeedbackModel.objects.all()
    serializer_class = CompUniFeedback
    permission_classes = [permissions.IsAuthenticated]


class CompUniFeedbackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompUniFeedbackModel.objects.all()
    serializer_class = CompUniFeedback
    permission_classes = [permissions.IsAuthenticated]
