from rest_framework import serializers
from app.models import UniversityTip


class UniversityTipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityTip
        fields = "__all__"
