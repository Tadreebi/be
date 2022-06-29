from rest_framework import serializers
from app.models import StudentGoal, StudentGoalIndicator


class StudentGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGoal
        fields = "__all__"


class StudentGoalIndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGoalIndicator
        fields = "__all__"
