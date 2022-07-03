from rest_framework import serializers
from app.models import StudentApplication,StudentApplicationResponse


class StudentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentApplication
        fields = "__all__"

class StudentApplicationResponseSerializer(serializers.ModelSerializer):
     class Meta:
        model = StudentApplicationResponse
        fields = "__all__"
