from rest_framework import serializers
from ...models.user_model import StudentUser, UniversityEmployeeUser, CompanyUser


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone",
            "address",
            "GPA",
            "major",
        )


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityEmployeeUser
        fields = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
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
            "first_name",
            "last_name",
            "phone",
            "address",
        )
