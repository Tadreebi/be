from rest_framework import serializers
from models import StudentReports, StudentReportSkills, StudentReportAchievements


class StudentReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReports
        fields = "__all__"


class StudentReportSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReportSkills
        fields = "__all__"


class StudentReportAchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReportAchievements
        fields = "__all__"
