from app.api.permissions import IsOwnerOrReadOnly
from app.api.serializers import (
    StudentReportAchievementsSerializer,
    StudentReportRemarksSerializer,
    StudentReportSkillsSerializer,
    StudentReportsSerializer,
    StudentReportTypesSerializer,
)
from app.models import (
    StudentReport,
    StudentReportAchievement,
    StudentReportRemark,
    StudentReportSkill,
    StudentReportType,
)
from rest_framework import generics, permissions
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
)


# Student Reports #########################################################
class StudentReportsList(ListAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportsCreate(ListCreateAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportsDetail(RetrieveAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportsDelete(RetrieveDestroyAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer

    permission_classes = [permissions.AllowAny]


# Student Report Types #########################################################
class StudentReportTypesList(ListAPIView):
    queryset = StudentReportType.objects.all()
    serializer_class = StudentReportTypesSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportTypesCreate(ListCreateAPIView):
    queryset = StudentReportType.objects.all()
    serializer_class = StudentReportTypesSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportTypesDetail(RetrieveAPIView):
    queryset = StudentReportType.objects.all()
    serializer_class = StudentReportTypesSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportTypesUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportType.objects.all()
    serializer_class = StudentReportTypesSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportTypesDelete(RetrieveDestroyAPIView):
    queryset = StudentReportType.objects.all()
    serializer_class = StudentReportTypesSerializer

    permission_classes = [permissions.AllowAny]


# Student Remarks #########################################################
class StudentReportRemarksList(ListAPIView):
    queryset = StudentReportRemark.objects.all()
    serializer_class = StudentReportRemarksSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportRemarksCreate(ListCreateAPIView):
    queryset = StudentReportRemark.objects.all()
    serializer_class = StudentReportRemarksSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportRemarksDetail(RetrieveAPIView):
    queryset = StudentReportRemark.objects.all()
    serializer_class = StudentReportRemarksSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportRemarksUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportRemark.objects.all()
    serializer_class = StudentReportRemarksSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportRemarksDelete(RetrieveDestroyAPIView):
    queryset = StudentReportRemark.objects.all()
    serializer_class = StudentReportRemarksSerializer

    permission_classes = [permissions.AllowAny]


# Student Report Skills ###################################################
class StudentReportSkillsList(ListAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportSkillsCreate(ListCreateAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportSkillsDetail(RetrieveAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportSkillsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportSkillsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer

    permission_classes = [permissions.AllowAny]


# Student Report Achievements #############################################
class StudentReportAchievementsList(ListAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportAchievementsCreate(ListCreateAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportAchievementsDetail(RetrieveAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportAchievementsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer

    permission_classes = [permissions.AllowAny]


class StudentReportAchievementsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer

    permission_classes = [permissions.AllowAny]
