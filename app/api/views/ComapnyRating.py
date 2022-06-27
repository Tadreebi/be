from app.models import ComapnyRating
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    ComapnyRatingSerializer,
)


class ComapnyRatingList(ListAPIView):
    queryset = ComapnyRating.objects.all()
    serializer_class = ComapnyRatingSerializer


class ComapnyRatingCreate(ListCreateAPIView):
    queryset = ComapnyRating.objects.all()
    serializer_class = ComapnyRatingSerializer


class ComapnyRatingDetail(RetrieveAPIView):
    queryset = ComapnyRating.objects.all()
    serializer_class = ComapnyRatingSerializer


class ComapnyRatingUpdate(RetrieveUpdateAPIView):
    queryset = ComapnyRating.objects.all()
    serializer_class = ComapnyRatingSerializer


class ComapnyRatingDelete(RetrieveDestroyAPIView):
    queryset = ComapnyRating.objects.all()
    serializer_class = ComapnyRatingSerializer
