from rest_framework import serializers
from app.models.InternshipPost import PostInternship

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostInternship
        fields = "__all__"