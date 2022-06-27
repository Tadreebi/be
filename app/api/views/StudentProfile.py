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

from app.api.permissions import IsOwnerOrReadOnly


class StudentProfileList(ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentProfileCreate(ListCreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentProfileDetail(RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentProfileUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentProfileDelete(RetrieveDestroyAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
