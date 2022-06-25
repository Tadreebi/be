from app.api.views.InternshipPost import (
    PostInternshipList,
    PostInternshipDetail,

)
from django.urls import path

urlpatterns = [
    # Post
    path(
        "",
        PostInternshipList.as_view(),
        name="Internship Posts List",
    ),
    # Get Put Delete
    path(
        "<int:pk>",
        PostInternshipDetail.as_view(),
        name="Internship Posts List",
    ),
]