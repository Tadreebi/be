from app.api.views import (
    ComapnyRatingList,
    ComapnyRatingCreate,
    ComapnyRatingDetail,
    ComapnyRatingUpdate,
    ComapnyRatingDelete,
)
from django.urls import path

urlpatterns = [
    path(
        "",
        ComapnyRatingList.as_view(),
        name="ComapnyRating Profile List",
    ),
    path(
        "create",
        ComapnyRatingCreate.as_view(),
        name="ComapnyRating Profile Create",
    ),
    path(
        "<int:pk>",
        ComapnyRatingDetail.as_view(),
        name="ComapnyRating Profile Details",
    ),
    path(
        "update/<int:pk>",
        ComapnyRatingUpdate.as_view(),
        name="ComapnyRating Profile Update",
    ),
    path(
        "delete/<int:pk>",
        ComapnyRatingDelete.as_view(),
        name="ComapnyRating Profile Delete",
    ),
]
