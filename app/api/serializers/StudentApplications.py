from rest_framework import serializers
from app.models import StudentApplications


class StudentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentApplications
        fields = "__all__"
