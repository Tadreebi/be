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

from ..permissions import IsOwnerOrReadOnly, CompanyPermission


class ApplicationResponseList(ListAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer
    permission_classes = [permissions.AllowAny]


class ApplicationResponseCreate(ListCreateAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer
    permission_classes = [IsOwnerOrReadOnly, CompanyPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ApplicationResponseDetail(RetrieveAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer
    permission_classes = [IsOwnerOrReadOnly, CompanyPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ApplicationResponseUpdate(RetrieveUpdateAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer
    permission_classes = [IsOwnerOrReadOnly, CompanyPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ApplicationResponseDelete(RetrieveDestroyAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer
    permission_classes = [IsOwnerOrReadOnly, CompanyPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
