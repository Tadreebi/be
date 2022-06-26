from app.api.views.attendance import (
    AttendanceList,
    AttendanceCreate,
    AttendanceDetail,
    AttendanceUpdate,
    AttendanceDelete,
)
from django.urls import path

urlpatterns = [
    path(
        "",
        AttendanceList.as_view(),
        name="Attendance List",
    ),
    path(
        "create",
        AttendanceCreate.as_view(),
        name="Attendance Create",
    ),
    path(
        "<int:pk>",
        AttendanceDetail.as_view(),
        name="Attendance Details",
    ),
    path(
        "update/<int:pk>",
        AttendanceUpdate.as_view(),
        name="Attendance Update",
    ),
    path(
        "delete/<int:pk>",
        AttendanceDelete.as_view(),
        name="Attendance Delete",
    ),
]
