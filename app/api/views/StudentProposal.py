from app.models import StudentUniProposal
from rest_framework.permissions import AllowAny

from app.api.serializers import (
    StudentprposalSerializer,

    
)

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework import generics, permissions


class ProposalPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "student":
            return True
        if request.user.type != "student" and request.method == "GET":
            return True
        return False

class Proposal_List_View(ListAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class = StudentprposalSerializer

    permission_classes = [permissions.AllowAny]


class proposal_create(ListCreateAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class = StudentprposalSerializer

    permission_classes = [permissions.AllowAny]


class proposal_detail_view(RetrieveAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class = StudentprposalSerializer

    permission_classes = [permissions.AllowAny]


class proposal_Update(RetrieveUpdateAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class = StudentprposalSerializer

    permission_classes = [permissions.AllowAny]


class proposal_delete(RetrieveDestroyAPIView):
    queryset = StudentUniProposal.objects.all()
    serializer_class = StudentprposalSerializer

    permission_classes = [permissions.AllowAny]
