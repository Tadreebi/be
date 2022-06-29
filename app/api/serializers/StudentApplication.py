from rest_framework import serializers
from app.models import StudentApplication


class StudentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentApplication
        fields = "__all__"
