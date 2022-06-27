from rest_framework import serializers
from app.models import InternshipPost, InternshipRequirements


class InternshipPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipPost
        fields = "__all__"


class InternshipRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipRequirements
        fields = "__all__"


# class ApplySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentApplication
#         fields = "__all__"

# class BrowseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BrowsePostsInternships
#         fields = "__all__"
