from django.contrib import admin
from app.models.StudentExperience import StudentExperience
from app.models import (
    StudentReport,
    StudentReportSkill,
    StudentReportAchievement,
    StudentProfile,

)

admin.site.register(StudentReport)
admin.site.register(StudentReportSkill)
admin.site.register(StudentReportAchievement)
admin.site.register(StudentProfile)
admin.site.register(StudentExperience)
