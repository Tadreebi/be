from rest_framework import serializers
from app.models import CompanyRating


class CompanyRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyRating
        fields = "__all__"
