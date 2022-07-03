from rest_framework import viewsets
from .FilterPosts import InternshipsFilter
from app.models import InternshipPost, InternshipRequirements
from app.api.serializers import (
    InternshipPostSerializer,
    InternshipRequirementsSerializer,
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import generics, permissions


# Internship Post #########################################################
# GET and POST
class InternshipPostList(ListCreateAPIView):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer
    permission_classes = [permissions.AllowAny]

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


# GET DELETE PUT
class InternshipPostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer
    permission_classes = [permissions.AllowAny]


# ViewSets
class InternshipPostsViewSets(viewsets.ModelViewSet):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer
    permission_classes = [permissions.AllowAny]


# Internship Post Requirements  #########################################################
# GET and POST
class InternshipPostRequirementsList(ListCreateAPIView):
    queryset = InternshipRequirements.objects.all()
    serializer_class = InternshipRequirementsSerializer
    permission_classes = [permissions.AllowAny]


# GET DELETE PUT
class InternshipPostRequirementsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = InternshipRequirements.objects.all()
    serializer_class = InternshipRequirementsSerializer
    permission_classes = [permissions.AllowAny]


# ViewSets
class InternshipPostRequirementsViewSets(viewsets.ModelViewSet):
    queryset = InternshipRequirements.objects.all()
    serializer_class = InternshipRequirementsSerializer
    permission_classes = [permissions.AllowAny]
