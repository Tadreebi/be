from rest_framework import generics, permissions
from ...additional_models.comp_uni_feedback import (
    CompUniFeedback as CompUniFeedbackModel,
)
from ..serializers.comp_uni_feedback import CompUniFeedback


class CompUniFeedbackListView(generics.ListCreateAPIView):
    queryset = CompUniFeedbackModel.objects.all()
    serializer_class = CompUniFeedback
    permission_classes = [permissions.IsAuthenticated]


class CompUniFeedbackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompUniFeedbackModel.objects.all()
    serializer_class = CompUniFeedback
    permission_classes = [permissions.IsAuthenticated]
