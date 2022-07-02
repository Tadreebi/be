from app.api.views import (
    UniversityTipsList,
    UniversityTipsCreate,
    UniversityTipsDetail,
    UniversityTipsUpdate,
    UniversityTipsDelete,
    UniversityTipTopicsList,
    UniversityTipTopicsCreate,
    UniversityTipTopicsDetail,
    UniversityTipTopicsUpdate,
    UniversityTipTopicsDelete,
)
from django.urls import path, re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path(
        "",
        UniversityTipsList.as_view(),
        name="University Tips List",
    ),
    path(
        "create/",
        UniversityTipsCreate.as_view(),
        name="University Tips Create",
    ),
    path(
        "<int:pk>",
        UniversityTipsDetail.as_view(),
        name="University Tips Details",
    ),
    path(
        "update/<int:pk>",
        UniversityTipsUpdate.as_view(),
        name="University Tips Update",
    ),
    path(
        "delete/<int:pk>",
        UniversityTipsDelete.as_view(),
        name="University Tips Delete",
    ),
    path(
        "topics/",
        UniversityTipTopicsList.as_view(),
        name=" University Tip Topics List",
    ),
    path(
        "topics/create/",
        UniversityTipTopicsCreate.as_view(),
        name=" University Tip Topics Create",
    ),
    path(
        "topics/<int:pk>",
        UniversityTipTopicsDetail.as_view(),
        name=" University Tip Topics Details",
    ),
    path(
        "topics/update/<int:pk>",
        UniversityTipTopicsUpdate.as_view(),
        name=" University Tip Topics Update",
    ),
    path(
        "topics/delete/<int:pk>",
        UniversityTipTopicsDelete.as_view(),
        name=" University Tip Topics Delete",
    ),
]
