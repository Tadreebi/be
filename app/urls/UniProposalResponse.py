from app.api.views import (
    UniResponse_Update,
    UniResponse_create,
    UniResponse_detail_view,
    UniResponse_List_View,
    UniResponse_delete,
)
from django.urls import path


urlpatterns = [
    path(
        "",
        UniResponse_List_View.as_view(),
        name="University proposal Response List",
    ),
    path(
        "create/",
        UniResponse_create.as_view(),
        name="University proposal Response Create",
    ),
    path(
        "<int:pk>",
        UniResponse_detail_view.as_view(),
        name="University proposal Response Details",
    ),
    path(
        "update/<int:pk>",
        UniResponse_Update.as_view(),
        name="University proposal Response Update",
    ),
    path(
        "delete/<int:pk>",
        UniResponse_delete.as_view(),
        name="University proposal Response Delete",
    ),
]
