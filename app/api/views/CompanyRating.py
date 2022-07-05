from app.models import CompanyRating
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    CompanyRatingSerializer,
)
from rest_framework import generics, permissions

from ..permissions import IsOwnerOrReadOnly, StudentPermission


class CompanyRatingList(ListAPIView):
    queryset = CompanyRating.objects.all()
    serializer_class = CompanyRatingSerializer

    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class CompanyRatingCreate(ListCreateAPIView):
    queryset = CompanyRating.objects.all()
    serializer_class = CompanyRatingSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class CompanyRatingDetail(RetrieveAPIView):
    queryset = CompanyRating.objects.all()
    serializer_class = CompanyRatingSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class CompanyRatingUpdate(RetrieveUpdateAPIView):
    queryset = CompanyRating.objects.all()
    serializer_class = CompanyRatingSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class CompanyRatingDelete(RetrieveDestroyAPIView):
    queryset = CompanyRating.objects.all()
    serializer_class = CompanyRatingSerializer
    
    # permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
