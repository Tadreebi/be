from app.models import StudentProfile
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    StudentProfileSerializer,
)


class StudentProfilesList(ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class StudentProfilesCreate(ListCreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class StudentProfilesDetail(RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class StudentProfilesUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class StudentProfilesDelete(RetrieveDestroyAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
