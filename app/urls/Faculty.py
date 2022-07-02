from django.urls import path
from app.api.views import (
    FacultyListView,
    FacultyDetailsView,
)

urlpatterns = [
    path(
        "",
        FacultyListView.as_view(),
        name="faculty_major_list",
    ),
    path(
        "<int:pk>",
        FacultyDetailsView.as_view(),
        name="faculty_major_detail",
    ),
]
