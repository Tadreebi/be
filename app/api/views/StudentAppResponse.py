from app.models import StudentApplicationResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    StudentApplicationResponseSerializer,
)
from rest_framework import generics, permissions


class ApplicationResponseList(ListAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ApplicationResponseCreate(ListCreateAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ApplicationResponseDetail(RetrieveAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ApplicationResponseUpdate(RetrieveUpdateAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ApplicationResponseDelete(RetrieveDestroyAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
