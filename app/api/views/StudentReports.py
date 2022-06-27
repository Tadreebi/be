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

# Student Reports #########################################################
class StudentReportsList(ListAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportsCreate(ListCreateAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportsDetail(RetrieveAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportsDelete(RetrieveDestroyAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# Student Report Skills ###################################################
class StudentReportSkillsList(ListAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportSkillsCreate(ListCreateAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportSkillsDetail(RetrieveAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportSkillsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportSkillsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# Student Report Achievements #############################################
class StudentReportAchievementsList(ListAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportAchievementsCreate(ListCreateAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportAchievementsDetail(RetrieveAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportAchievementsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class StudentReportAchievementsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer
    permission_classes = (IsOwnerOrReadOnly,)
