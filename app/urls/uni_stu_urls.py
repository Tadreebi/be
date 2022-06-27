from django.urls import path
from app.api.views import (
    UniStuFeedbackListView,
    UniStuFeedbackDetailsView,
)

urlpatterns = [
    path(
        "uni-stu-feedback/",
        UniStuFeedbackListView.as_view(),
        name="uni_stu_feedback_list",
    ),
    path(
        "uni-stu-feedback/<int:pk>/",
        UniStuFeedbackDetailsView.as_view(),
        name="uni_stu_feedback_detail",
    ),
]
