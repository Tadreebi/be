from django.urls import path, re_path
from django.views.generic.base import RedirectView
from rest_framework_simplejwt import views as jwt_views

from app.api.views import (
    StudentReportsList,
    StudentReportsCreate,
    StudentReportsDetail,
    StudentReportsUpdate,
    StudentReportsDelete,
    StudentReportSkillsList,
    StudentReportSkillsCreate,
    StudentReportSkillsDetail,
    StudentReportSkillsUpdate,
    StudentReportSkillsDelete,
    StudentReportAchievementsList,
    StudentReportAchievementsCreate,
    StudentReportAchievementsDetail,
    StudentReportAchievementsUpdate,
    StudentReportAchievementsDelete,
)

urlpatterns = [
    path(
        "/",
        StudentReportsList.as_view(),
        name="Student Reports List",
    ),
    path(
        "/create",
        StudentReportsCreate.as_view(),
        name="Student Reports Create",
    ),
    path(
        "/<int:pk>",
        StudentReportsDetail.as_view(),
        name="Student Reports Details",
    ),
    path(
        "/update/<int:pk>",
        StudentReportsUpdate.as_view(),
        name="Student Reports Update",
    ),
    path(
        "/delete/<int:pk>",
        StudentReportsDelete.as_view(),
        name="Student Reports Delete",
    ),
    path(
        "/skills",
        StudentReportSkillsList.as_view(),
        name="Student Report Skills List",
    ),
    path(
        "/skills/create",
        StudentReportSkillsCreate.as_view(),
        name="Student Report Skills Create",
    ),
    path(
        "/skills/<int:pk>",
        StudentReportSkillsDetail.as_view(),
        name="Student Report Skills Details",
    ),
    path(
        "/skills/update/<int:pk>",
        StudentReportSkillsUpdate.as_view(),
        name="Student Report Skills Update",
    ),
    path(
        "/skills/delete/<int:pk>",
        StudentReportSkillsDelete.as_view(),
        name="Student Report Skills Delete",
    ),
    path(
        "/achievements",
        StudentReportAchievementsList.as_view(),
        name="Student Report Achievements List",
    ),
    path(
        "/achievements/create",
        StudentReportAchievementsCreate.as_view(),
        name="Student Report Achievements Create",
    ),
    path(
        "/achievements/<int:pk>",
        StudentReportAchievementsDetail.as_view(),
        name="Student Report Achievements Details",
    ),
    path(
        "/achievements/update/<int:pk>",
        StudentReportAchievementsUpdate.as_view(),
        name="Student Report Achievements Update",
    ),
    path(
        "/achievements/delete/<int:pk>",
        StudentReportAchievementsDelete.as_view(),
        name="Student Report Achievements Delete",
    ),
    re_path(
        r"^.*$",
        RedirectView.as_view(url="api/v1/currencies/", permanent=False),
        name="Redirect",
    ),
]
