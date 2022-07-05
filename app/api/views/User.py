from rest_framework import generics, permissions
from app.models import StudentUser, UniversityEmployeeUser, CompanyUser
from app.api.serializers import (
    StudentSerializer,
    UniversitySerializer,
    CompanySerializer,
)


# Student views and permissions


class PermissionStudentSignUp(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "Student":
            return True
        return False


class StudentSignUpView(generics.ListCreateAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentSerializer
    
    # permission_classes = [PermissionStudentSignUp]
    permission_classes = [permissions.AllowAny]


class StudentSignUpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentSerializer
    
    # permission_classes = [PermissionStudentSignUp]
    permission_classes = [permissions.AllowAny]
    lookup_field = "username"


# University employee views and permissions


class PermissionUniversitySignUp(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "University Employee":
            return True
        return False


class UniversitySignUpView(generics.ListCreateAPIView):
    queryset = UniversityEmployeeUser.objects.all()
    serializer_class = UniversitySerializer
    
    # permission_classes = [PermissionUniversitySignUp]
    permission_classes = [permissions.AllowAny]


class UniversitySignUpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniversityEmployeeUser.objects.all()
    serializer_class = UniversitySerializer
    
    # permission_classes = [PermissionUniversitySignUp]
    permission_classes = [permissions.AllowAny]
    lookup_field = "username"


# Company views and permissions


class PermissionCompanySignUp(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "Company":
            return True
        return False


class CompanySignUpView(generics.ListCreateAPIView):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanySerializer
    
    # permission_classes = [PermissionCompanySignUp]
    permission_classes = [permissions.AllowAny]


class CompanySignUpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanySerializer
    
    # permission_classes = [PermissionCompanySignUp]
    permission_classes = [permissions.AllowAny]
    lookup_field = "username"
