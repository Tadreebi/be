from django.urls import path
from app.api.views import (
    UniversityFeedbackList,
    UniversityFeedbackCreate,
    UniversityFeedbackDetail,
    UniversityFeedbackUpdate,
    UniversityFeedbackDelete,
)

urlpatterns = [
    path(
        "",
        UniversityFeedbackList.as_view(),
        name="University Feedbacks List",
    ),
    path(
        "<int:pk>",
        UniversityFeedbackDetail.as_view(),
        name="University Feedback Details",
    ),
    path(
        "create/",
        UniversityFeedbackCreate.as_view(),
        name="University Feedback Create",
    ),
    path(
        "update/<int:pk>",
        UniversityFeedbackUpdate.as_view(),
        name="University Feedback Update",
    ),
    path(
        "delete/<int:pk>",
        UniversityFeedbackDelete.as_view(),
        name="University Feedback Delete",
    ),
]
