from rest_framework import serializers
from app.models.StudentProposal import StudentUniProposal

class StudentprposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUniProposal
        fields = "__all__"