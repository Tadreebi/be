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


class CompanyReportList(ListAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer


class CompanyReportCreate(ListCreateAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer


class CompanyReportDetail(RetrieveAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer


class CompanyReportUpdate(RetrieveUpdateAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer


class CompanyReportDelete(RetrieveDestroyAPIView):
    queryset = CompanyReport.objects.all()
    serializer_class = CompanyReportSerializer
