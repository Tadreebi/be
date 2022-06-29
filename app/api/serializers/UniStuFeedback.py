from rest_framework import serializers
from app.models import UniStuFeedback


class UniStuFeedback(serializers.ModelSerializer):
    class Meta:
        model = UniStuFeedback
        fields = "__all__"
