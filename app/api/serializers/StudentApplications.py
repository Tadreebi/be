from rest_framework import serializers
from app.models.StudentApplications import StudentApplications
from app.api.serializers.InternshipPost import PostSerializer

class StudentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentApplications
        fields = '__all__'