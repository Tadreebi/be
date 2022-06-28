from app.api.views import (
    CompanyReportList,
    CompanyReportCreate,
    CompanyReportDetail,
    CompanyReportUpdate,
    CompanyReportDelete,
)
from django.urls import path

urlpatterns = [
    path(
        "",
        CompanyReportList.as_view(),
        name="Report List",
    ),
    path(
        "create/",
        CompanyReportCreate.as_view(),
        name="Report Create",
    ),
    path(
        "<int:pk>",
        CompanyReportDetail.as_view(),
        name="Report Details",
    ),
    path(
        "update/<int:pk>",
        CompanyReportUpdate.as_view(),
        name="Report Update",
    ),
    path(
        "delete/<int:pk>",
        CompanyReportDelete.as_view(),
        name="Report Delete",
    ),
]
