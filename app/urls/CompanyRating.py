from app.api.views import (
    CompanyRatingList,
    CompanyRatingCreate,
    CompanyRatingDetail,
    CompanyRatingUpdate,
    CompanyRatingDelete,
)
from django.urls import path

urlpatterns = [
    path(
        "",
    CompanyRatingList.as_view(),
        name="CompanyRating Profile List",
    ),
    path(
        "create/",
    CompanyRatingCreate.as_view(),
        name="CompanyRating Profile Create",
    ),
    path(
        "<int:pk>",
    CompanyRatingDetail.as_view(),
        name="CompanyRating Profile Details",
    ),
    path(
        "update/<int:pk>",
    CompanyRatingUpdate.as_view(),
        name="CompanyRating Profile Update",
    ),
    path(
        "delete/<int:pk>",
    CompanyRatingDelete.as_view(),
        name="CompanyRating Profile Delete",
    ),
]
