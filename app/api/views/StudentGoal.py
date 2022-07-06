from app.models import StudentGoal, StudentGoalIndicator
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    StudentGoalIndicatorsSerializer,
    StudentGoalsSerializer,
)
from rest_framework import generics, permissions

from ..permissions import IsOwner, StudentStrictPermission


# Student Reports #########################################################
class StudentGoalsList(ListAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer
    permission_classes = [permissions.AllowAny]


class StudentGoalsCreate(ListCreateAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentGoalsDetail(RetrieveAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentGoalsUpdate(RetrieveUpdateAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentGoalsDelete(RetrieveDestroyAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Student Report Skills ###################################################
class StudentGoalIndicatorsList(ListAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer
    permission_classes = [permissions.AllowAny]


class StudentGoalIndicatorsCreate(ListCreateAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentGoalIndicatorsDetail(RetrieveAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentGoalIndicatorsUpdate(RetrieveUpdateAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudentGoalIndicatorsDelete(RetrieveDestroyAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
