from rest_framework import permissions

# Very general
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# # University User permissions
# class UniversityPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "University Employee":
#             return True
#         return False


# class UniversityReadOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if (
#             request.user.type == "University Employee"
#             and request.method in permissions.SAFE_METHODS
#         ):
#             return True
#         return False


# class UniversityAddOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "University Employee" and request.method is "POST":
#             return True
#         return False


# class UniversitychangeonlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "University Employee" and request.method is "PUT":
#             return True
#         return False


# class UniversityDeleteOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "University Employee" and request.method is "DELETE":
#             return True
#         return False


# # Student User permissions
# class StudentPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "Student":
#             return True
#         return False


# class StudentReadOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if (
#             request.user.type == "Student"
#             and request.method in permissions.SAFE_METHODS
#         ):
#             return True
#         return False


# class StudentAddOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "Student" and request.method is "POST":
#             return True
#         return False


# class StudentchangeonlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "Student" and request.method is "PUT":
#             return True
#         return False


# class StudentDeleteOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "Student" and request.method is "DELETE":
#             return True
#         return False


# # Company User permissions
# class CompanyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "Company":
#             return True
#         return False


# class CompanyReadOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if (
#             request.user.type == "Company"
#             and request.method in permissions.SAFE_METHODS
#         ):
#             return True
#         return False


# class CompanyAddOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "Company" and request.method is "POST":
#             return True
#         return False


# class CompanychangeonlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "Company" and request.method is "PUT":
#             return True
#         return False


# class CompanyDeleteOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type == "Company" and request.method is "DELETE":
#             return True
#         return False
