from rest_framework import serializers
from app.models import UniversityFeedback


class UniversityFeedback(serializers.ModelSerializer):
    class Meta:
        model = UniversityFeedback
        fields = "__all__"
