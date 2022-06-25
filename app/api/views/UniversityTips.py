from app.api.serializers import UniversityTipsSerializer
from app.models import UniversityTip
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
)


class UniversityTipsList(ListAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer


class UniversityTipsCreate(ListCreateAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer


class UniversityTipsDetail(RetrieveAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer


class UniversityTipsUpdate(RetrieveUpdateAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer


class UniversityTipsDelete(RetrieveDestroyAPIView):
    queryset = UniversityTip.objects.all()
    serializer_class = UniversityTipsSerializer
