from rest_framework import serializers
from app.models import UniversityTip, UniversityTipTopic


class UniversityTipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityTip
        fields = "__all__"


class UniversityTipTopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityTipTopic
        fields = "__all__"
