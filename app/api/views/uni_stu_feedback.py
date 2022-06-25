from rest_framework import generics, permissions
from ...additional_models.uni_stu_feedback import UniStuFeedback as UniStuFeedbackModel
from ..serializers.uni_stu_feedback import UniStuFeedback


class UniStuFeedbackListView(generics.ListCreateAPIView):
    queryset = UniStuFeedbackModel.objects.all()
    serializer_class = UniStuFeedback
    permission_classes = [permissions.IsAuthenticated]


class UniStuFeedbackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniStuFeedbackModel.objects.all()
    serializer_class = UniStuFeedback
    permission_classes = [permissions.IsAuthenticated]
