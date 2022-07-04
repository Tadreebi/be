from rest_framework import viewsets
from app.models import (
    StudentApplication,
    StudentApplicationResponse
    )
from app.api.serializers import (
    StudentApplicationSerializer, StudentApplicationResponseSerializer
    )
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework import generics, permissions

# Students Application
class StudentApplicationList(ListAPIView):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer

    permission_classes = [permissions.AllowAny]

class StudentApplicationCreate(ListCreateAPIView):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer

    permission_classes = [permissions.AllowAny]

class StudentApplicationDetail(RetrieveAPIView):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer

    permission_classes = [permissions.AllowAny]

class StudentApplicationUpdate(RetrieveUpdateAPIView):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer

    permission_classes = [permissions.AllowAny]

class StudentApplicationDelete(RetrieveDestroyAPIView):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer

    permission_classes = [permissions.AllowAny]

# Students Application ViewSets
class ApplicationsViewSets(viewsets.ModelViewSet):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer
    permission_classes = [permissions.AllowAny]

# StudentApplicationResponse

class StudentApplicationResponseList(ListAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer

    permission_classes = [permissions.AllowAny]

class StudentApplicationResponseCreate(ListCreateAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer

    permission_classes = [permissions.AllowAny]

class StudentApplicationResponseDetail(RetrieveAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer

    permission_classes = [permissions.AllowAny]

class StudentApplicationResponseUpdate(RetrieveUpdateAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer

    permission_classes = [permissions.AllowAny]

class StudentApplicationResponseDelete(RetrieveDestroyAPIView):
    queryset = StudentApplicationResponse.objects.all()
    serializer_class = StudentApplicationResponseSerializer

    permission_classes = [permissions.AllowAny]