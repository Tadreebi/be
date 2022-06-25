from app.models.rating import Rating
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers.rating import (
    RatingSerializer,
)


class RatingList(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RatingCreate(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RatingDetail(RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RatingUpdate(RetrieveUpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RatingDelete(RetrieveDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

