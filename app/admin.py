from django.contrib import admin
from app.models import (
    StudentReport,
    StudentReportSkill,
    StudentReportAchievement,
    StudentProfile,
    UniversityTip,
)

admin.site.register(StudentReport)
admin.site.register(StudentReportSkill)
admin.site.register(StudentReportAchievement)
admin.site.register(StudentProfile)

admin.site.register(UniversityTip)
