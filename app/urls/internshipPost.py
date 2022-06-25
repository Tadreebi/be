from app.api.views.InternshipPost import (
    PostInternshipList,

)
from django.urls import path

urlpatterns = [
    path(
        "",
        PostInternshipList.as_view(),
        name="Internship Posts List",
    ),
]