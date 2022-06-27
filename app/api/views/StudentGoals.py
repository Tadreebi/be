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

# Student Reports #########################################################
class StudentGoalsList(ListAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer


class StudentGoalsCreate(ListCreateAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer


class StudentGoalsDetail(RetrieveAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer


class StudentGoalsUpdate(RetrieveUpdateAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer


class StudentGoalsDelete(RetrieveDestroyAPIView):
    queryset = StudentGoal.objects.all()
    serializer_class = StudentGoalsSerializer


# Student Report Skills ###################################################
class StudentGoalIndicatorsList(ListAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer


class StudentGoalIndicatorsCreate(ListCreateAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer


class StudentGoalIndicatorsDetail(RetrieveAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer


class StudentGoalIndicatorsUpdate(RetrieveUpdateAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer


class StudentGoalIndicatorsDelete(RetrieveDestroyAPIView):
    queryset = StudentGoalIndicator.objects.all()
    serializer_class = StudentGoalIndicatorsSerializer
