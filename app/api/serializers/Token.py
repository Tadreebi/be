from rest_framework_simplejwt.serializers import (
    TokenObtainSerializer,
    RefreshToken,
    api_settings,
    update_last_login,
)
from django.core import serializers
from app.models.User import StudentUser, UniversityEmployeeUser, CompanyUser


class TokenSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        serialized_student_user = serializers.serialize("json", StudentUser)
        student_user = serialized_student_user.objects.filter(pk=self.user.id).first()

        serialized_university_employee_user = serializers.serialize(
            "json", UniversityEmployeeUser
        )
        university_employee_user = serialized_university_employee_user.objects.filter(
            pk=self.user.id
        ).first()

        serialized_company_user = serializers.serialize("json", CompanyUser)
        company_user = serialized_company_user.objects.filter(pk=self.user.id).first()

        if student_user:
            data["user"] = student_user
        elif university_employee_user:
            data["user"] = university_employee_user
        elif company_user:
            data["user"] = company_user
        else:
            data["user"] = None

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
