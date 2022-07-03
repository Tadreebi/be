from rest_framework import generics, permissions
from app.models import Faculty
from app.api.serializers import FacultySerializer


class PermissionFacultyListView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "University Employee":
            return True
        if request.user.type != "University Employee" and request.method == "GET":
            return True
        return False


class FacultyListView(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [PermissionFacultyListView]


class PermissionFacultyDetailsView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "University Employee":
            return True
        return False


class FacultyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [PermissionFacultyDetailsView]
