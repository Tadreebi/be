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


# University Tips #########################################################
class UniversityTipsList(ListAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipsCreate(ListCreateAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipsDetail(RetrieveAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipsUpdate(RetrieveUpdateAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipsDelete(RetrieveDestroyAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
    permission_classes = [permissions.IsAuthenticated]


# University Topic Tips #########################################################
class UniversityTipTopicsList(ListAPIView):
    queryset = UniversityTipTopic.objects.all()
    serializer_class = UniversityTipTopicsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipTopicsCreate(ListCreateAPIView):
    queryset = UniversityTipTopic.objects.all()
    serializer_class = UniversityTipTopicsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipTopicsDetail(RetrieveAPIView):
    queryset = UniversityTipTopic.objects.all()
    serializer_class = UniversityTipTopicsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipTopicsUpdate(RetrieveUpdateAPIView):
    queryset = UniversityTipTopic.objects.all()
    serializer_class = UniversityTipTopicsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityTipTopicsDelete(RetrieveDestroyAPIView):
    queryset = UniversityTipTopic.objects.all()
    serializer_class = UniversityTipTopicsSerializer
    permission_classes = [permissions.IsAuthenticated]
