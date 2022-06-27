from app.models import StudentExperience
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers.StudentExperience import (
    StudentExperienceSerializer,
)

class StudentExperienceList(ListAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer
    permission_classes= IsAuthenticatedOrReadOnly


class StudentExperienceCreate(ListCreateAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer
    permission_classes= IsAuthenticatedOrReadOnly


class StudentExperienceDetail(RetrieveAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer
    permission_classes= IsAuthenticatedOrReadOnly


class StudentExperienceUpdate(RetrieveUpdateAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer
    permission_classes= IsAuthenticatedOrReadOnly


class StudentExperienceDelete(RetrieveDestroyAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer
    permission_classes= IsAuthenticatedOrReadOnly
