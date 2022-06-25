from rest_framework import serializers
from app.models.InternshipPost import PostInternship

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostInternship
        fields = "__all__"

# class ApplySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentApplication
#         fields = "__all__"

# class BrowseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BrowsePostsInternships
#         fields = "__all__"