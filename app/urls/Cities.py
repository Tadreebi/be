from app.api.views import (
    CitiesDelete,
    CitiesCreate,
    CitiesDetail,
    CitiesList,
    CitiesUpdate
)
from django.urls import path

urlpatterns = [
    path(
        "",
        CitiesList.as_view(),
        name="Cities List",
    ),
    path(
        "create/",
        CitiesCreate.as_view(),
        name="Cities Create",
    ),
    path(
        "<int:pk>",
        CitiesDetail.as_view(),
        name="Cities Details",
    ),
    path(
        "update/<int:pk>",
        CitiesUpdate.as_view(),
        name="Cities Update",
    ),
    path(
        "delete/<int:pk>",
        CitiesDelete.as_view(),
        name="Cities Delete",
    ),
]
