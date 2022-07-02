from rest_framework import serializers
from app.models import StudentUser, UniversityEmployeeUser, CompanyUser


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = (
            "id",
            "username",
            "email",
            "password",
            "name",
            "phone",
            "address",
            "GPA",
            "faculty",
            "type",
        )


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityEmployeeUser
        fields = (
            "id",
            "username",
            "email",
            "password",
            "name",
            "phone",
            "address",
            "type",
        )


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = (
            "id",
            "username",
            "email",
            "password",
            "name",
            "phone",
            "address",
            "about",
            "type",
        )
