from rest_framework import generics, permissions
from app.models import StudentUser, UniversityEmployeeUser, CompanyUser
from app.api.serializers import (
    StudentSerializer,
    UniversitySerializer,
    CompanySerializer,
)


class StudentSignUpView(generics.ListCreateAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversitySignUpView(generics.ListCreateAPIView):
    queryset = UniversityEmployeeUser.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanySignUpView(generics.ListCreateAPIView):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentSignUpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "username"


class UniversitySignUpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniversityEmployeeUser.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "username"


class CompanySignUpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "username"
