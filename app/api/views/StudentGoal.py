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

# Student Reports #########################################################
class StudentGoalsList(ListAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentGoalsCreate(ListCreateAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentGoalsDetail(RetrieveAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentGoalsUpdate(RetrieveUpdateAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentGoalsDelete(RetrieveDestroyAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer
    permission_classes = [permissions.IsAuthenticated]


# Student Report Skills ###################################################
class StudentGoalIndicatorsList(ListAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentGoalIndicatorsCreate(ListCreateAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentGoalIndicatorsDetail(RetrieveAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentGoalIndicatorsUpdate(RetrieveUpdateAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentGoalIndicatorsDelete(RetrieveDestroyAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer
    permission_classes = [permissions.IsAuthenticated]
