from app.models.StudentProposal import StudentUniProposal
from app.api.serializers.StudentProposal import StudentprposalSerializer
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

class Proposal_List_View(ListAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class=StudentprposalSerializer

class proposal_create(ListCreateAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class=StudentprposalSerializer

class proposal_detail_view(RetrieveAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class=StudentprposalSerializer

class proposal_Update(RetrieveUpdateAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class=StudentprposalSerializer

class proposal_delete(RetrieveDestroyAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class=StudentprposalSerializer



