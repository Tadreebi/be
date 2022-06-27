from django.contrib import admin
from app.models import (
    StudentUser,
    CompanyUser,
    UniversityEmployeeUser,
    UniStuFeedback,
    CompUniFeedback,
    AppUser,
    StudentProfile,
    StudentReport,
    StudentReportAchievement,
    StudentReportSkill,
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
