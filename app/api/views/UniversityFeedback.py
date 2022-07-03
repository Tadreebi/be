from rest_framework import generics, permissions
from app.models import UniversityFeedback
from app.api.serializers import UniversityFeedbackSerializer


class PermissionUniversityFeedbackListView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.type == "University Employee":
            return True
        if request.user.type != "University Employee" and request.method == "GET":
            return True
        return False


class UniversityFeedbackListView(generics.ListCreateAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    permission_classes = [PermissionUniversityFeedbackListView]


class PermissionUniversityFeedbackDetailsView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.type == "University Employee":
            return True
        return False


class UniversityFeedbackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    permission_classes = [PermissionUniversityFeedbackDetailsView]
