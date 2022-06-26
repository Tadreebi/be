from app.models.StudentExperience import StudentExperience
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


class StudentExperienceCreate(ListCreateAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer


class StudentExperienceDetail(RetrieveAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer


class StudentExperienceUpdate(RetrieveUpdateAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer


class StudentExperienceDelete(RetrieveDestroyAPIView):
    queryset = StudentExperience.objects.all()
    serializer_class = StudentExperienceSerializer
