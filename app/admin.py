from django.contrib import admin

from app.models import (
    StudentProfile,
    StudentReport,
    StudentReportAchievement,
    StudentReportSkill,
)

from app.models import AppUser


@admin.register(AppUser)
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


admin.site.register(StudentReport)
admin.site.register(StudentReportSkill)
admin.site.register(StudentReportAchievement)
admin.site.register(StudentProfile)
