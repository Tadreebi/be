from app.api.views import (
    ApplicationResponseUpdate,
    ApplicationResponseList,
    ApplicationResponseCreate,
    ApplicationResponseDelete,
    ApplicationResponseDetail,

)
from django.urls import path


urlpatterns = [
    path(
        "",
        ApplicationResponseList.as_view(),
        name="Application Response List",
    ),
    path(
        "create/",
        ApplicationResponseCreate.as_view(),
        name="Application Response Create",
    ),
    path(
        "<int:pk>",
        ApplicationResponseDetail.as_view(),
        name="Application Response Details",
    ),
    path(
        "update/<int:pk>",
        ApplicationResponseUpdate.as_view(),
        name="Application Response Update",
    ),
    path(
        "delete/<int:pk>",
        ApplicationResponseDelete.as_view(),
        name="Application Response Delete",
    ),
]
