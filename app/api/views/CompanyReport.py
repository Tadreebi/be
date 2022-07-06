from app.models import CompanyReport
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    CompanyReportSerializer,
)
from rest_framework import generics, permissions

from ..permissions import IsOwnerOrReadOnly, CompanyPermission


class CompanyReportList(ListAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer
    permission_classes = [permissions.AllowAny]


class CompanyReportCreate(ListCreateAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CompanyReportDetail(RetrieveAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CompanyReportUpdate(RetrieveUpdateAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CompanyReportDelete(RetrieveDestroyAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
