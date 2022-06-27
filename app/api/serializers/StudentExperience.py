from rest_framework import serializers
from app.models import StudentExperience


class StudentExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExperience
        fields = "__all__"

