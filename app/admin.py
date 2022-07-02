from django.contrib import admin

from app.models import (
    AppUser,
    ComapnyRating,
    CompanyReport,
    InternshipPost,
    StudentApplication,
    StudentExperience,
    StudentGoal,
    StudentGoalIndicator,
    StudentProfile,
    StudentUniProposal,
    StudentReport,
    StudentReportSkill,
    StudentReportAchievement,
    UniversityFeedback,
    UniversityTip,
    StudentUser,
    CompanyUser,
    UniversityEmployeeUser,
    Faculty,
    SupervisedBy,
)


@admin.register(UniversityEmployeeUser)
class AdminUniversityEmployeeUser(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "is_admin",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("is_admin", "is_active", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("username",)


@admin.register(CompanyUser)
class AdminCompanyUser(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "is_admin",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("is_admin", "is_active", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("username",)


@admin.register(StudentUser)
class AdminStudentUser(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "is_admin",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("is_admin", "is_active", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("username",)


admin.site.register(ComapnyRating)
admin.site.register(CompanyReport)
admin.site.register(InternshipPost)
admin.site.register(StudentApplication)
admin.site.register(StudentExperience)
admin.site.register(StudentGoal)
admin.site.register(StudentGoalIndicator)
admin.site.register(StudentProfile)
admin.site.register(StudentUniProposal)
admin.site.register(StudentReport)
admin.site.register(StudentReportSkill)
admin.site.register(StudentReportAchievement)
admin.site.register(UniversityFeedback)
admin.site.register(UniversityTip)
admin.site.register(Faculty)
admin.site.register(SupervisedBy)
