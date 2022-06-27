from app.models.report import Report
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers.report import (
    ReportSerializer,
)


class ReportList(ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportCreate(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetail(RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportUpdate(RetrieveUpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDelete(RetrieveDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
