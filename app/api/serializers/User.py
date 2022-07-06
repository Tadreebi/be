from rest_framework import serializers
from app.models import StudentUser, UniversityEmployeeUser, CompanyUser


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser

        fields = "__all__"

class StudentUsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = "username"


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityEmployeeUser

        fields = "__all__"


class UniversityEmployee1UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityEmployeeUser
        fields = "username"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser

        fields = "__all__"


class CompanyUsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = "username"
