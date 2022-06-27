from rest_framework import viewsets
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


# Internship Post #########################################################
# GET and POST
class InternshipPostList(ListCreateAPIView):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer

    def list(self, request, *args, **kw):
        queries = request.query_params

        list_queries = {
            f"{query}": queries.get(query).upper()
            for query in queries
            if (query in ("education", "industry", "experience"))
        }

        queryset = (
            PostInternship.objects.filter(**list_queries)
            if list_queries
            else PostInternship.objects.all()
        )

        return Response({queryset.values()})


# GET DELETE PUT
class InternshipPostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer


# ViewSets
class InternshipPostsViewSets(viewsets.ModelViewSet):
    queryset = InternshipPost.objects.all()
    serializer_class = InternshipPostSerializer


# Internship Post Requirements  #########################################################
# GET and POST
class InternshipPostRequirementsList(ListCreateAPIView):
    queryset = InternshipRequirements.objects.all()
    serializer_class = InternshipRequirementsSerializer


# GET DELETE PUT
class InternshipPostRequirementsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = InternshipRequirements.objects.all()
    serializer_class = InternshipRequirementsSerializer


# ViewSets
class InternshipPostRequirementsViewSets(viewsets.ModelViewSet):
    queryset = InternshipRequirements.objects.all()
    serializer_class = InternshipRequirementsSerializer
