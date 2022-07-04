from rest_framework import viewsets
from .FilterPosts import InternshipsFilter
from app.models import InternshipPost
from app.api.serializers import (
    InternshipPostSerializer,
)
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import generics, permissions

from ..permissions import IsOwnerOrReadOnly, CompanyPermission


# Internship Post
class InternshipPostList(ListAPIView):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer
    permission_classes = [IsOwnerOrReadOnly, CompanyPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kw):
        queries = request.query_params

        list_queries = {
            f"{query}": queries.get(query).upper()
            for query in queries
            if (query in ("education", "industry"))
        }

        queryset = (
            InternshipPost.objects.filter(**list_queries)
            if list_queries
            else InternshipPost.objects.all()
        )

        return Response({queryset.values()})


class InternshipPostCreate(ListCreateAPIView):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class InternshipPostDetail(RetrieveAPIView):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer
    permission_classes = [IsOwnerOrReadOnly, CompanyPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class InternshipPostUpdate(RetrieveUpdateAPIView):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class InternshipPostDelete(RetrieveDestroyAPIView):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# ViewSets
class InternshipPostsViewSets(viewsets.ModelViewSet):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer
    permission_classes = [IsOwnerOrReadOnly, CompanyPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
