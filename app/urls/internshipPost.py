from app.api.views.InternshipPost import (
    PostInternshipList,
    PostInternshipRetrieveUpdateDestroy,

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
        PostInternshipRetrieveUpdateDestroy.as_view(),
        name="Internship Posts Delete Update Get",
    ),
]