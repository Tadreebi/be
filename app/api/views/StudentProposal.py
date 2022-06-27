from app.models import StudentUniProposal
from app.api.permissions.permissions import IsAuthenticatedOrReadOnly

from app.api.serializers.StudentProposal import (
    StudentprposalSerializer,
)

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
    permission_classes = [IsAuthenticatedOrReadOnly]

class proposal_create(ListCreateAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class=StudentprposalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class proposal_detail_view(RetrieveAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class=StudentprposalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class proposal_Update(RetrieveUpdateAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class=StudentprposalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class proposal_delete(RetrieveDestroyAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class=StudentprposalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


