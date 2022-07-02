from app.api.views import (
    StudentReportAchievementsCreate,
    StudentReportAchievementsDelete,
    StudentReportAchievementsDetail,
    StudentReportAchievementsList,
    StudentReportAchievementsUpdate,
    StudentReportsCreate,
    StudentReportsDelete,
    StudentReportsDetail,
    StudentReportSkillsCreate,
    StudentReportSkillsDelete,
    StudentReportSkillsDetail,
    StudentReportSkillsList,
    StudentReportSkillsUpdate,
    StudentReportsList,
    StudentReportsUpdate,
    StudentReportRemarksList,
    StudentReportRemarksCreate,
    StudentReportRemarksDetail,
    StudentReportRemarksUpdate,
    StudentReportRemarksDelete,
)
from django.urls import path, re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path(
        "reports/",
        StudentReportsList.as_view(),
        name="Student Reports List",
    ),
    path(
        "reports/create/",
        StudentReportsCreate.as_view(),
        name="Student Reports Create",
    ),
    path(
        "reports/<int:pk>",
        StudentReportsDetail.as_view(),
        name="Student Reports Details",
    ),
    path(
        "reports/update/<int:pk>",
        StudentReportsUpdate.as_view(),
        name="Student Reports Update",
    ),
    path(
        "reports/delete/<int:pk>",
        StudentReportsDelete.as_view(),
        name="Student Reports Delete",
    ),
    path(
        "remarks/",
        StudentReportRemarksList.as_view(),
        name="Student Report Remarks List",
    ),
    path(
        "remarks/create/",
        StudentReportRemarksCreate.as_view(),
        name="Student Report Remarks Create",
    ),
    path(
        "remarks/<int:pk>",
        StudentReportRemarksDetail.as_view(),
        name="Student Report Remarks Details",
    ),
    path(
        "remarks/update/<int:pk>",
        StudentReportRemarksUpdate.as_view(),
        name="Student Report Remarks Update",
    ),
    path(
        "remarks/delete/<int:pk>",
        StudentReportRemarksDelete.as_view(),
        name="Student Report Remarks Delete",
    ),
    path(
        "skills/",
        StudentReportSkillsList.as_view(),
        name="Student Report Skills List",
    ),
    path(
        "skills/create/",
        StudentReportSkillsCreate.as_view(),
        name="Student Report Skills Create",
    ),
    path(
        "skills/<int:pk>",
        StudentReportSkillsDetail.as_view(),
        name="Student Report Skills Details",
    ),
    path(
        "skills/update/<int:pk>",
        StudentReportSkillsUpdate.as_view(),
        name="Student Report Skills Update",
    ),
    path(
        "skills/delete/<int:pk>",
        StudentReportSkillsDelete.as_view(),
        name="Student Report Skills Delete",
    ),
    path(
        "achievements/",
        StudentReportAchievementsList.as_view(),
        name="Student Report Achievements List",
    ),
    path(
        "achievements/create/",
        StudentReportAchievementsCreate.as_view(),
        name="Student Report Achievements Create",
    ),
    path(
        "achievements/<int:pk>",
        StudentReportAchievementsDetail.as_view(),
        name="Student Report Achievements Details",
    ),
    path(
        "achievements/update/<int:pk>",
        StudentReportAchievementsUpdate.as_view(),
        name="Student Report Achievements Update",
    ),
    path(
        "achievements/delete/<int:pk>",
        StudentReportAchievementsDelete.as_view(),
        name="Student Report Achievements Delete",
    ),
]
