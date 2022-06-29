from app.api.views import (
    StudentGoalIndicatorsCreate,
    StudentGoalIndicatorsDelete,
    StudentGoalIndicatorsDetail,
    StudentGoalIndicatorsList,
    StudentGoalIndicatorsUpdate,
    StudentGoalsCreate,
    StudentGoalsDelete,
    StudentGoalsDetail,
    StudentGoalsList,
    StudentGoalsUpdate,
)
from django.urls import path, re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path(
        "",
        StudentGoalsList.as_view(),
        name="Student Goals List",
    ),
    path(
        "create/",
        StudentGoalsCreate.as_view(),
        name="Student Goals Create",
    ),
    path(
        "<int:pk>",
        StudentGoalsDetail.as_view(),
        name="Student Goals Details",
    ),
    path(
        "update/<int:pk>",
        StudentGoalsUpdate.as_view(),
        name="Student Goals Update",
    ),
    path(
        "delete/<int:pk>",
        StudentGoalsDelete.as_view(),
        name="Student Goals Delete",
    ),
    path(
        "indicators/",
        StudentGoalIndicatorsList.as_view(),
        name="Student Goal Indicators List",
    ),
    path(
        "indicators/create/",
        StudentGoalIndicatorsCreate.as_view(),
        name="Student Goal Indicators Create",
    ),
    path(
        "indicators/<int:pk>",
        StudentGoalIndicatorsDetail.as_view(),
        name="Student Goal Indicators Details",
    ),
    path(
        "indicators/update/<int:pk>",
        StudentGoalIndicatorsUpdate.as_view(),
        name="Student Goal Indicators Update",
    ),
    path(
        "indicators/delete/<int:pk>",
        StudentGoalIndicatorsDelete.as_view(),
        name="Student Goal Indicators Delete",
    ),
]
