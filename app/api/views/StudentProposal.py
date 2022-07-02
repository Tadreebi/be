from app.models import StudentUniProposal,UniProposalResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.api.serializers import (
    StudentprposalSerializer,
    UniProposalResponseSerializer
    
)

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework import generics, permissions


class Proposal_List_View(ListAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class = StudentprposalSerializer

    permission_classes = [permissions.IsAuthenticated]


class proposal_create(ListCreateAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class = StudentprposalSerializer

    permission_classes = [permissions.IsAuthenticated]


class proposal_detail_view(RetrieveAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class = StudentprposalSerializer

    permission_classes = [permissions.IsAuthenticated]


class proposal_Update(RetrieveUpdateAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class = StudentprposalSerializer

    permission_classes = [permissions.IsAuthenticated]


class proposal_delete(RetrieveDestroyAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class = StudentprposalSerializer

    permission_classes = [permissions.IsAuthenticated]



# Uni Response Views

class UniResponse_List_View(ListAPIView):
    queryset = UniProposalResponse.objects.all()
    serializer_class = UniProposalResponseSerializer

    permission_classes = [permissions.IsAuthenticated]


class UniResponse_create(ListCreateAPIView):
    queryset = UniProposalResponse.objects.all()
    serializer_class = UniProposalResponseSerializer

    permission_classes = [permissions.IsAuthenticated]


class UniResponse_detail_view(RetrieveAPIView):
    queryset = UniProposalResponse.objects.all()
    serializer_class = UniProposalResponseSerializer

    permission_classes = [permissions.IsAuthenticated]


class UniResponse_Update(RetrieveUpdateAPIView):
    queryset = UniProposalResponse.objects.all()
    serializer_class = UniProposalResponseSerializer

    permission_classes = [permissions.IsAuthenticated]


class UniResponse_delete(RetrieveDestroyAPIView):
    queryset = UniProposalResponse.objects.all()
    serializer_class = UniProposalResponseSerializer

    permission_classes = [permissions.IsAuthenticated]

