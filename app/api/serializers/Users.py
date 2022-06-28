from rest_framework import serializers
from app.models import StudentUser, UniversityEmployeeUser, CompanyUser


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = "__all__"


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityEmployeeUser
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = "__all__"
