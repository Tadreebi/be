from app.api.views import (
    StudentProfileList,
    StudentProfileCreate,
    StudentProfileDetail,
    StudentProfileUpdate,
    StudentProfileDelete,
)
from django.urls import path

urlpatterns = [
    path(
        "",
        StudentProfileList.as_view(),
        name="Student Profile List",
    ),
    path(
        "create",
        StudentProfileCreate.as_view(),
        name="Student Profile Create",
    ),
    path(
        "<int:pk>",
        StudentProfileDetail.as_view(),
        name="Student Profile Details",
    ),
    path(
        "update/<int:pk>",
        StudentProfileUpdate.as_view(),
        name="Student Profile Update",
    ),
    path(
        "delete/<int:pk>",
        StudentProfileDelete.as_view(),
        name="Student Profile Delete",
    ),
]
