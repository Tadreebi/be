from django.contrib import admin

from app.models import (
    AppUser,
    ComapnyRating,
    CompUniFeedback,
    CompanyReport,
    InternshipPost,
    StudentApplications,
    StudentExperience,
    StudentGoal,
    StudentGoalIndicator,
    StudentProfile,
    StudentUniProposal,
    StudentReport,
    StudentReportSkill,
    StudentReportAchievement,
    UniStuFeedback,
    UniversityTip,
    StudentUser,
    CompanyUser,
    UniversityEmployeeUser,
)


@admin.register(UniversityEmployeeUser)
class AdminAppUser(admin.ModelAdmin):
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
class AdminAppUser(admin.ModelAdmin):
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
class AdminAppUser(admin.ModelAdmin):
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
admin.site.register(CompUniFeedback)
admin.site.register(CompanyReport)
admin.site.register(InternshipPost)
admin.site.register(StudentApplications)
admin.site.register(StudentExperience)
admin.site.register(StudentGoal)
admin.site.register(StudentGoalIndicator)
admin.site.register(StudentProfile)
admin.site.register(StudentUniProposal)
admin.site.register(StudentReport)
admin.site.register(StudentReportSkill)
admin.site.register(StudentReportAchievement)
admin.site.register(UniStuFeedback)
admin.site.register(UniversityTip)
