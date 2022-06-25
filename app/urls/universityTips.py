from app.api.views import (
    UniversityTipsList,
    UniversityTipsCreate,
    UniversityTipsDetail,
    UniversityTipsUpdate,
    UniversityTipsDelete,
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
]
