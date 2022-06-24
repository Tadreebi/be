from rest_framework import serializers
from app.models import StudenProfile


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudenProfile
        fields = "__all__"
