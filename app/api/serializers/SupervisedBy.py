from rest_framework import serializers
from app.models import SupervisedBy


class SupervisedBySerializer(serializers.Serializer):
    class Meta:
        model = SupervisedBy
        fields = "__all__"
