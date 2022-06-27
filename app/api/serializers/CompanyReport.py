from rest_framework import serializers
from app.models import CompanyReport


class CompanyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyReport
        fields = "__all__"
