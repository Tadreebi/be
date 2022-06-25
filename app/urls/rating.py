from app.api.views.rating import (
    RatingList,
    RatingCreate,
    RatingDetail,
    RatingUpdate,
    RatingDelete,
)
from django.urls import path

urlpatterns = [
    path(
        "",
        RatingList.as_view(),
        name="Rating Profile List",
    ),
    path(
        "create",
        RatingCreate.as_view(),
        name="Rating Profile Create",
    ),
    path(
        "<int:pk>",
        RatingDetail.as_view(),
        name="Rating Profile Details",
    ),
    path(
        "update/<int:pk>",
        RatingUpdate.as_view(),
        name="Rating Profile Update",
    ),
    path(
        "delete/<int:pk>",
        RatingDelete.as_view(),
        name="Rating Profile Delete",
    ),
]