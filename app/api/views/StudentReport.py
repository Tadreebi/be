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

from app.api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions

# Student Reports #########################################################
class StudentReportsList(ListAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportsCreate(ListCreateAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportsDetail(RetrieveAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportsDelete(RetrieveDestroyAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer

    permission_classes = [permissions.IsAuthenticated]


# Student Report Skills ###################################################
class StudentReportSkillsList(ListAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportSkillsCreate(ListCreateAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportSkillsDetail(RetrieveAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportSkillsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportSkillsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer

    permission_classes = [permissions.IsAuthenticated]


# Student Report Achievements #############################################
class StudentReportAchievementsList(ListAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportAchievementsCreate(ListCreateAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportAchievementsDetail(RetrieveAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportAchievementsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentReportAchievementsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer

    permission_classes = [permissions.IsAuthenticated]
