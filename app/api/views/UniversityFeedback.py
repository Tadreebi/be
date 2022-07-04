from app.api.serializers import UniversityFeedbackSerializer
from app.models import UniversityFeedback
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
)


class PermissionUniversityFeedbackListView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "University Employee":
            return True
        if request.user.type != "University Employee" and request.method == "GET":
            return True
        return False


class UniversityFeedbackList(ListAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer

    permission_classes = [PermissionUniversityFeedbackListView]


class PermissionUniversityFeedbackDetailsView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "University Employee":
            return True
        return False


class UniversityFeedbackCreate(ListCreateAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer

    permission_classes = [PermissionUniversityFeedbackDetailsView]


class UniversityFeedbackDetail(RetrieveAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer

    permission_classes = [PermissionUniversityFeedbackDetailsView]


class UniversityFeedbackUpdate(RetrieveUpdateAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer

    permission_classes = [PermissionUniversityFeedbackDetailsView]


class UniversityFeedbackDelete(RetrieveDestroyAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer

    permission_classes = [PermissionUniversityFeedbackDetailsView]
