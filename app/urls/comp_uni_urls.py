from django.urls import path
from app.api.views import (
    CompUniFeedbackListView,
    CompUniFeedbackDetailsView,
)

urlpatterns = [
    path(
        "",
        CompUniFeedbackListView.as_view(),
        name="comp_uni_feedback_list",
    ),
    path(
        "<int:pk>",
        CompUniFeedbackDetailsView.as_view(),
        name="comp_uni_feedback_detail",
    ),
]
