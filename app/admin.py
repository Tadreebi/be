from django.contrib import admin
from app.models import StudentReport, StudentReportSkill, StudentReportAchievement

admin.site.register(StudentReport)
admin.site.register(StudentReportSkill)
admin.site.register(StudentReportAchievement)
