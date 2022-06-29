from app.api.views import (
    StudentExperienceCreate,
    StudentExperienceDelete,
    StudentExperienceDetail,
    StudentExperienceList,
    StudentExperienceUpdate,
)
from django.urls import path


urlpatterns = [
    path(
        "",
        StudentExperienceList.as_view(),
        name="Student Experience List",
    ),
    path(
        "create/",
        StudentExperienceCreate.as_view(),
        name="Student Experience Create",
    ),
    path(
        "<int:pk>",
        StudentExperienceDetail.as_view(),
        name="Student Experience Details",
    ),
    path(
        "update/<int:pk>",
        StudentExperienceUpdate.as_view(),
        name="Student Experience Update",
    ),
    path(
        "delete/<int:pk>",
        StudentExperienceDelete.as_view(),
        name="Student Experience Delete",
    ),
]
