from rest_framework import serializers
from app.models import ComapnyRating


class ComapnyRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComapnyRating
        fields = "__all__"
