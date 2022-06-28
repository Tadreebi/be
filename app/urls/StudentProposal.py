from django.urls import path
from app.api.views import (
    Proposal_List_View,
    proposal_Update,
    proposal_create,
    proposal_delete,
    proposal_detail_view,
)

urlpatterns = [
    path(
        "",
        Proposal_List_View.as_view(),
        name="Student proposal List",
    ),
    path(
        "create/",
        proposal_create.as_view(),
        name="Student proposal create",
    ),
    path(
        "<int:pk>",
        proposal_detail_view.as_view(),
        name="Student Proposal Detail",
    ),
    path(
        "update/<int:pk>",
        proposal_Update.as_view(),
        name="Student proposal update",
    ),
    path(
        "delete/<int:pk>",
        proposal_delete.as_view(),
        name="Student proposal update",
    ),
]
