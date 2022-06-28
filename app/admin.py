from django.contrib import admin

from app.models import (
    AppUser,
    StudentUser,
    UniversityEmployeeUser,
    CompanyUser,
    UniStuFeedback,
    CompUniFeedback,
    StudentReport,
    StudentReportSkill,
    StudentReportAchievement,
    StudentProfile,
    UniversityTip,
    StudentGoal,
    StudentGoalIndicator,
    StudentExperience,
    StudentUniProposal,
    ComapnyRating,
    CompanyReport,
    InternshipPost,
    StudentApplications,
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


admin.site.register(UniStuFeedback)
admin.site.register(CompUniFeedback)
admin.site.register(StudentReport)
admin.site.register(StudentReportSkill)
admin.site.register(StudentReportAchievement)
admin.site.register(StudentProfile)
admin.site.register(UniversityTip)
admin.site.register(StudentGoal)
admin.site.register(StudentGoalIndicator)
admin.site.register(InternshipPost)
admin.site.register(StudentApplications)
admin.site.register(CompanyReport)
admin.site.register(ComapnyRating)
admin.site.register(StudentExperience)
admin.site.register(StudentUniProposal)
