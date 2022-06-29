from django.urls import path
from app.api.views import (
    UniStuFeedbackListView,
    UniStuFeedbackDetailsView,
)

urlpatterns = [
    path(
        "",
        UniStuFeedbackListView.as_view(),
        name="uni_stu_feedback_list",
    ),
    path(
        "<int:pk>",
        UniStuFeedbackDetailsView.as_view(),
        name="uni_stu_feedback_detail",
    ),
]
