from app.models import StudentReportAchievement, StudentReport, StudentReportSkill
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    StudentReportAchievementsSerializer,
    StudentReportSkillsSerializer,
    StudentReportsSerializer,
)

# Student Reports #########################################################
class StudentReportsList(ListAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer


class StudentReportsCreate(ListCreateAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer


class StudentReportsDetail(RetrieveAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer


class StudentReportsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer


class StudentReportsDelete(RetrieveDestroyAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer


# Student Report Skills ###################################################
class StudentReportSkillsList(ListAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer


class StudentReportSkillsCreate(ListCreateAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer


class StudentReportSkillsDetail(RetrieveAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer


class StudentReportSkillsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer


class StudentReportSkillsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer


# Student Report Achievements #############################################
class StudentReportAchievementsList(ListAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer


class StudentReportAchievementsCreate(ListCreateAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer


class StudentReportAchievementsDetail(RetrieveAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer


class StudentReportAchievementsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer


class StudentReportAchievementsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer
