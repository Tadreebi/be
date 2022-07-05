from rest_framework import generics, permissions
from app.models import SupervisedBy
from app.api.serializers import SupervisedBySerializer


class PermissionSupervisedByListView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "University Employee":
            return True
        if request.user.type != "University Employee" and request.method == "GET":
            return True
        return False


class SupervisedByListView(generics.ListCreateAPIView):
    queryset = SupervisedBy.objects.all()
    serializer_class = SupervisedBySerializer
    permission_classes = [PermissionSupervisedByListView]


class PermissionSupervisedByDetailsView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "University Employee":
            return True
        return False


class SupervisedByDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupervisedBy.objects.all()
    serializer_class = SupervisedBySerializer
    permission_classes = [PermissionSupervisedByDetailsView]
