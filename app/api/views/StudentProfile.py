from app.models import StudenProfile
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
    queryset = StudenProfile.objects.all()
    serializer_class = StudentProfileSerializer


class StudentProfilesCreate(ListCreateAPIView):
    queryset = StudenProfile.objects.all()
    serializer_class = StudentProfileSerializer


class StudentProfilesDetail(RetrieveAPIView):
    queryset = StudenProfile.objects.all()
    serializer_class = StudentProfileSerializer


class StudentProfilesUpdate(RetrieveUpdateAPIView):
    queryset = StudenProfile.objects.all()
    serializer_class = StudentProfileSerializer


class StudentProfilesDelete(RetrieveDestroyAPIView):
    queryset = StudenProfile.objects.all()
    serializer_class = StudentProfileSerializer
