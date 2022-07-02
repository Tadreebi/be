from rest_framework import serializers
from app.models import UniversityFeedback


class UniversityFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityFeedback
        fields = "__all__"
