from rest_framework import serializers
from app.models import (
    StudentReport,
    StudentReportSkill,
    StudentReportAchievement,
    StudentReportRemark,
)


class StudentReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReport
        fields = "__all__"


class StudentReportRemarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReportRemark
        fields = "__all__"


class StudentReportSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReportSkill
        fields = "__all__"


class StudentReportAchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReportAchievement
        fields = "__all__"
