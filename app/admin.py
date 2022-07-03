from django.contrib import admin

from app.models import (
    AppUser,
    ComapnyRating,
    CompanyReport,
    CompanyUser,
    Faculty,
    InternshipPost,
    StudentApplication,
    StudentExperience,
    StudentGoal,
    StudentGoalIndicator,
    StudentProfile,
    StudentProfileContact,
    StudentProfileEducation,
    StudentProfileExperience,
    StudentProfileLanguage,
    StudentProfileSkill,
    StudentProfileWork,
    StudentReportType,
    StudentReport,
    StudentReportRemark,
    StudentReportSkill,
    StudentReportAchievement,
    StudentUniProposal,
    StudentUser,
    SupervisedBy,
    UniversityEmployeeUser,
    UniversityFeedback,
    UniversityTip,
    StudentApplicationResponse
    
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
admin.site.register(StudentReportType)
admin.site.register(StudentProfileExperience)
admin.site.register(StudentProfileSkill)
admin.site.register(StudentProfileEducation)
admin.site.register(StudentProfileLanguage)
admin.site.register(StudentProfileContact)
admin.site.register(StudentProfileWork)
admin.site.register(StudentUniProposal)
admin.site.register(StudentReport)
admin.site.register(StudentReportRemark)
admin.site.register(StudentReportSkill)
admin.site.register(StudentReportAchievement)
admin.site.register(UniversityFeedback)
admin.site.register(UniversityTip)
admin.site.register(Faculty)
admin.site.register(SupervisedBy)
admin.site.register(StudentApplicationResponse)

