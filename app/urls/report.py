from app.api.views.report import (
    ReportList,
    ReportCreate,
    ReportDetail,
    ReportUpdate,
    ReportDelete,
)
from django.urls import path

urlpatterns = [
    path(
        "",
        ReportList.as_view(),
        name="Report List",
    ),
    path(
        "create",
        ReportCreate.as_view(),
        name="Report Create",
    ),
    path(
        "<int:pk>",
        ReportDetail.as_view(),
        name="Report Details",
    ),
    path(
        "update/<int:pk>",
        ReportUpdate.as_view(),
        name="Report Update",
    ),
    path(
        "delete/<int:pk>",
        ReportDelete.as_view(),
        name="Report Delete",
    ),
]
