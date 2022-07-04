from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """anyone can read but only the auther can add/edit/delete"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsOwner(permissions.BasePermission):
    """only the owner can read/create/edit/delete, for private pages"""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class UniversityPermission(permissions.BasePermission):
    """Any user can read but only the university user can add/edit/delete"""

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "University Employee":
            return True
        if (
            request.user.type != "University Employee"
            and request.method in permissions.SAFE_METHODS
        ):
            return True
        return False


class UniversityStrictPermission(permissions.BasePermission):
    """Only the university user can read/add/edit/delete"""

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "University Employee":
            return True
        return False


class StudentPermission(permissions.BasePermission):
    """Any user can read but only the student user can add/edit/delete"""

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "Student":
            return True
        if (
            request.user.type != "Student"
            and request.method in permissions.SAFE_METHODS
        ):
            return True
        return False


class StudentStrictPermission(permissions.BasePermission):
    """Only the student user can read/add/edit/delete"""

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "Student":
            return True
        return False


class CompanyPermission(permissions.BasePermission):
    """Any user can read but only the company user can add/edit/delete"""

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "Company":
            return True
        if (
            request.user.type != "Company"
            and request.method in permissions.SAFE_METHODS
        ):
            return True
        return False


class CompanyStrictPermission(permissions.BasePermission):
    """Only the company user can read/add/edit/delete"""

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.type == "Company":
            return True
        return False
