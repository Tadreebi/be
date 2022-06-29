from django.urls import path
from app.api.views import (
    UniversityFeedbackListView,
    UniversityFeedbackDetailsView,
)

urlpatterns = [
    path(
        "",
        UniversityFeedbackListView.as_view(),
        name="uni_stu_feedback_list",
    ),
    path(
        "<int:pk>",
        UniversityFeedbackDetailsView.as_view(),
        name="uni_stu_feedback_detail",
    ),
]
