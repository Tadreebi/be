from rest_framework import viewsets
from app.models import StudentApplications
from app.api.serializers import StudentApplicationSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


# GET and POST
class StudentApplicationsList(ListCreateAPIView):
    queryset = StudentApplications.objects.all()
    serializer_class = StudentApplicationSerializer


# GET DELETE PUT
class StudentApplicationsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = StudentApplications.objects.all()
    serializer_class = StudentApplicationSerializer


# ViewSets
class ApplicationsViewSets(viewsets.ModelViewSet):
    queryset = StudentApplications.objects.all()
    serializer_class = StudentApplicationSerializer
