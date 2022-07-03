from rest_framework import permissions

# Very general
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# Example
class PermissionExample(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "University Employee":
            return True
        if request.user.type != "University Employee" and request.method == "GET":
            return True
        return False
