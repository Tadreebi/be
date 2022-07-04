from app.models import UniProposalResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.api.serializers import UniProposalResponseSerializer

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework import generics, permissions

from ..permissions import IsOwnerOrReadOnly, UniversityPermission


class UniResponse_List_View(ListAPIView):
    queryset = UniProposalResponse.objects.all()
    serializer_class = UniProposalResponseSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniResponse_create(ListCreateAPIView):
    queryset = UniProposalResponse.objects.all()
    serializer_class = UniProposalResponseSerializer
    permission_classes = [IsOwnerOrReadOnly, UniversityPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UniResponse_detail_view(RetrieveAPIView):
    queryset = UniProposalResponse.objects.all()
    serializer_class = UniProposalResponseSerializer
    permission_classes = [IsOwnerOrReadOnly, UniversityPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UniResponse_Update(RetrieveUpdateAPIView):
    queryset = UniProposalResponse.objects.all()
    serializer_class = UniProposalResponseSerializer
    permission_classes = [IsOwnerOrReadOnly, UniversityPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UniResponse_delete(RetrieveDestroyAPIView):
    queryset = UniProposalResponse.objects.all()
    serializer_class = UniProposalResponseSerializer
    permission_classes = [IsOwnerOrReadOnly, UniversityPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
