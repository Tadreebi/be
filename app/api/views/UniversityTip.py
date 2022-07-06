from app.api.serializers import UniversityTipsSerializer, UniversityTipTopicsSerializer
from app.models import UniversityTip, UniversityTipTopic
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework import generics, permissions
from ..permissions import IsOwnerOrReadOnly, UniversityPermission

# University Tips #########################################################
class UniversityTipsList(ListAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.AllowAny]


class UniversityTipsCreate(ListCreateAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UniversityTipsDetail(RetrieveAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UniversityTipsUpdate(RetrieveUpdateAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UniversityTipsDelete(RetrieveDestroyAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# University Topic Tips #########################################################
class UniversityTipTopicsList(ListAPIView):
    queryset = UniversityTipTopic.objects.all()
    serializer_class = UniversityTipTopicsSerializer
    permission_classes = [permissions.AllowAny]


class UniversityTipTopicsCreate(ListCreateAPIView):
    queryset = UniversityTipTopic.objects.all()
    serializer_class = UniversityTipTopicsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UniversityTipTopicsDetail(RetrieveAPIView):
    queryset = UniversityTipTopic.objects.all()
    serializer_class = UniversityTipTopicsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UniversityTipTopicsUpdate(RetrieveUpdateAPIView):
    queryset = UniversityTipTopic.objects.all()
    serializer_class = UniversityTipTopicsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UniversityTipTopicsDelete(RetrieveDestroyAPIView):
    queryset = UniversityTipTopic.objects.all()
    serializer_class = UniversityTipTopicsSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
