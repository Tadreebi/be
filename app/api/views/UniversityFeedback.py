from django.forms import ModelForm
from rest_framework import generics, permissions
from app.models import UniversityFeedback
from app.api.serializers import UniversityFeedbackSerializer
from ..permissions import (
    IsOwnerOrReadOnly,
    UniversityStrictPermission,
)


# class PermissionUniversityFeedbackListView(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.is_superuser:
#             return True
#         if request.user.type == "University Employee":
#             return True
#         if request.user.type != "University Employee" and request.method == "GET":
#             return True
#         return False


# class UniversityFeedbackForm(ModelForm):
#     class Meta:
#         model = UniversityFeedback
#         fields = "__all__"


class UniversityFeedbackListView(generics.ListCreateAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    # from_class = UniversityFeedbackForm
    # permission_classes = [PermissionUniversityFeedbackListView]
    # permission_classes = [permissions.AllowAny]
    permission_classes = [UniversityStrictPermission, IsOwnerOrReadOnly]

    # def form_valid(self, form, UniversityFeedbackForm):
    #     obj = form.save(commit=False)
    #     obj.author = self.request.user
    #     obj.save()
    #     return super().form_valid(form)


# class PermissionUniversityFeedbackDetailsView(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.is_superuser:
#             return True
#         if request.user.type == "University Employee":
#             return True
#         return False


class UniversityFeedbackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniversityFeedback.objects.all()
    serializer_class = UniversityFeedbackSerializer
    # permission_classes = [PermissionUniversityFeedbackDetailsView]
    # permission_classes = [permissions.AllowAny]
    permission_classes = [UniversityStrictPermission, IsOwnerOrReadOnly]
