from app.api.views import (
    StudentApplicationList,
    StudentApplicationCreate,
    StudentApplicationDetail,
    StudentApplicationUpdate,
    StudentApplicationDelete,
    StudentApplicationResponseList,
    StudentApplicationResponseCreate,
    StudentApplicationResponseDetail,
    StudentApplicationResponseUpdate,
    StudentApplicationResponseDelete,
    # ApplicationsViewSets,
)
from django.urls import path, include
# from rest_framework.routers import DefaultRouter

# # Viewsets Route
# router = DefaultRouter()
# router.register("applied", ApplicationsViewSets)

urlpatterns = [
    path(
        "applications/",
        StudentApplicationList.as_view(),
        name="Student Applications List",
    ),
    path(
        "applications/create/",
        StudentApplicationCreate.as_view(),
        name="Student Applications Create",
    ),
    path(
        "applications/<int:pk>",
        StudentApplicationDetail.as_view(),
        name="Student Applications Details",
    ),
    path(
        "applications/update/<int:pk>",
        StudentApplicationUpdate.as_view(),
        name="Student Applications Update",
    ),
    path(
        "applications/delete/<int:pk>",
        StudentApplicationDelete.as_view(),
        name="Student Applications Delete",
    ),
    # # Viewsets
    # path(
    #     "",
    #     include(router.urls),
    # ),
    path(
        "responses/",
        StudentApplicationResponseList.as_view(),
        name="Student Responses List",
    ),
    path(
        "responses/create/",
        StudentApplicationResponseCreate.as_view(),
        name="Student Responses Create",
    ),
    path(
        "responses/<int:pk>",
        StudentApplicationResponseDetail.as_view(),
        name="Student Responses Details",
    ),
    path(
        "responses/update/<int:pk>",
        StudentApplicationResponseUpdate.as_view(),
        name="Student Responses Update",
    ),
    path(
        "responses/delete/<int:pk>",
        StudentApplicationResponseDelete.as_view(),
        name="Student Responses Delete",
    ),
]
