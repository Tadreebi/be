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
            # "first_name",
            # "last_name",
            "name",
            "phone",
            "address",
            "GPA",
            "faculty",
        )


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityEmployeeUser
        fields = (
            "id",
            "username",
            "email",
            "password",
            # "first_name",
            # "last_name",
            "name",
            "phone",
            "address",
        )


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = (
            "id",
            "username",
            "email",
            "password",
            # "first_name",
            # "last_name",
            "name",
            "phone",
            "address",
            "about",
        )
