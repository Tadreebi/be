from rest_framework import serializers
from ...models.comp_uni_feedback import CompUniFeedback


class CompUniFeedback(serializers.ModelSerializer):
    class Meta:
        model = CompUniFeedback
        fields = (
            "id",
            "student_username",
            "feedback",
            "date",
            "rating",
        )