from django.contrib import admin
from .models import StudentReports, StudentReportSkills, StudentReportAchievements

admin.site.register(StudentReports)
admin.site.register(StudentReportSkills)
admin.site.register(StudentReportAchievements)
