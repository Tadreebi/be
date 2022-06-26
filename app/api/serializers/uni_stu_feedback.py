from rest_framework import serializers
from ...models.uni_stu_feedback import UniStuFeedback


class UniStuFeedback(serializers.ModelSerializer):
    class Meta:
        model = UniStuFeedback
        fields = (
            "id",
            "student_username",
            "feedback",
            "date",
            "rating",
        )
