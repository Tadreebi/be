from django.urls import path
from ..api.views.comp_uni_feedback import (
    CompUniFeedbackListView,
    CompUniFeedbackDetailsView,
)

urlpatterns = [
    path(
        "comp-uni-feedback/",
        CompUniFeedbackListView.as_view(),
        name="comp_uni_feedback_list",
    ),
    path(
        "comp-uni-feedback/<int:pk>/",
        CompUniFeedbackDetailsView.as_view(),
        name="comp_uni_feedback_detail",
    ),
]
