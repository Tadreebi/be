from ..permissions import IsOwnerOrReadOnly, StudentPermission
from app.api.serializers import (
    StudentReportAchievementsSerializer,
    StudentReportRemarksSerializer,
    StudentReportSkillsSerializer,
    StudentReportsSerializer,
)
from app.models import (
    StudentReport,
    StudentReportAchievement,
    StudentReportRemark,
    StudentReportSkill,
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
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportsDetail(RetrieveAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportsDelete(RetrieveDestroyAPIView):
    queryset = StudentReport.objects.all()
    serializer_class = StudentReportsSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Student Remarks #########################################################
class StudentReportRemarksList(ListAPIView):
    queryset = StudentReportRemark.objects.all()
    serializer_class = StudentReportRemarksSerializer
    permission_classes = [permissions.AllowAny]


class StudentReportRemarksCreate(ListCreateAPIView):
    queryset = StudentReportRemark.objects.all()
    serializer_class = StudentReportRemarksSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportRemarksDetail(RetrieveAPIView):
    queryset = StudentReportRemark.objects.all()
    serializer_class = StudentReportRemarksSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportRemarksUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportRemark.objects.all()
    serializer_class = StudentReportRemarksSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportRemarksDelete(RetrieveDestroyAPIView):
    queryset = StudentReportRemark.objects.all()
    serializer_class = StudentReportRemarksSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Student Report Skills ###################################################
class StudentReportSkillsList(ListAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer
    permission_classes = [permissions.AllowAny]


class StudentReportSkillsCreate(ListCreateAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportSkillsDetail(RetrieveAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportSkillsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportSkillsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportSkill.objects.all()
    serializer_class = StudentReportSkillsSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Student Report Achievements #############################################
class StudentReportAchievementsList(ListAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer
    permission_classes = [permissions.AllowAny]


class StudentReportAchievementsCreate(ListCreateAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportAchievementsDetail(RetrieveAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportAchievementsUpdate(RetrieveUpdateAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentReportAchievementsDelete(RetrieveDestroyAPIView):
    queryset = StudentReportAchievement.objects.all()
    serializer_class = StudentReportAchievementsSerializer
    permission_classes = [IsOwnerOrReadOnly, StudentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
