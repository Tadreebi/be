from rest_framework import serializers
from app.models import StudentUniProposal,UniProposalResponse

class StudentprposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUniProposal
        fields = "__all__"

class UniProposalResponseSerializer(serializers.ModelSerializer):  
     class Meta:
        model = UniProposalResponse
        fields = "__all__"