from rest_framework import viewsets
from app.models import StudentApplication
from app.api.serializers import StudentApplicationSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import generics, permissions


# GET and POST
class StudentApplicationsList(ListCreateAPIView):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]


# GET DELETE PUT
class StudentApplicationsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]


# ViewSets
class ApplicationsViewSets(viewsets.ModelViewSet):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
