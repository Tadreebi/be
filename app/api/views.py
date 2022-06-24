from models import StudentReportAchievements, StudentReports, StudentReportSkills
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from .serializers import (
    StudentReportAchievementsSerializer,
    StudentReportSkillsSerializer,
    StudentReportsSerializer,
)

# Student Reports #########################################################
class StudentReportsList(ListAPIView):
    queryset = StudentReports.objects.all()
    serializer_class = StudentReportsSerializer


class StudentReportsCreate(ListCreateAPIView):
    queryset = StudentReports.objects.all()
    serializer_class = StudentReportsSerializer


class StudentReportsDetail(RetrieveAPIView):
    queryset = StudentReports.objects.all()
    serializer_class = StudentReportsSerializer


class StudentReportsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReports.objects.all()
    serializer_class = StudentReportsSerializer


class StudentReportsDelete(RetrieveDestroyAPIView):
    queryset = StudentReports.objects.all()
    serializer_class = StudentReportsSerializer


# Student Report Skills ###################################################
class StudentReportSkillsList(ListAPIView):
    queryset = StudentReportSkills.objects.all()
    serializer_class = StudentReportSkillsSerializer


class StudentReportSkillsCreate(ListCreateAPIView):
    queryset = StudentReportSkills.objects.all()
    serializer_class = StudentReportSkillsSerializer


class StudentReportSkillsDetail(RetrieveAPIView):
    queryset = StudentReportSkills.objects.all()
    serializer_class = StudentReportSkillsSerializer


class StudentReportSkillsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportSkills.objects.all()
    serializer_class = StudentReportSkillsSerializer


class StudentReportSkillsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportSkills.objects.all()
    serializer_class = StudentReportSkillsSerializer


# Student Report Achievements #############################################
class StudentReportAchievementsList(ListAPIView):
    queryset = StudentReportAchievements.objects.all()
    serializer_class = StudentReportAchievementsSerializer


class StudentReportAchievementsCreate(ListCreateAPIView):
    queryset = StudentReportAchievements.objects.all()
    serializer_class = StudentReportAchievementsSerializer


class StudentReportAchievementsDetail(RetrieveAPIView):
    queryset = StudentReportAchievements.objects.all()
    serializer_class = StudentReportAchievementsSerializer


class StudentReportAchievementsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportAchievements.objects.all()
    serializer_class = StudentReportAchievementsSerializer


class StudentReportAchievementsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportAchievements.objects.all()
    serializer_class = StudentReportAchievementsSerializer
