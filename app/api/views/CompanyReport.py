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


class CompanyReportList(ListAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer
    permission_classes = [permissions.AllowAny]


class CompanyReportCreate(ListCreateAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer
    permission_classes = [permissions.AllowAny]


class CompanyReportDetail(RetrieveAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer
    permission_classes = [permissions.AllowAny]


class CompanyReportUpdate(RetrieveUpdateAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer
    permission_classes = [permissions.AllowAny]


class CompanyReportDelete(RetrieveDestroyAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer
    permission_classes = [permissions.AllowAny]
