from django.contrib import admin
from app.models import (
    StudentReport,
    StudentReportSkill,
    StudentReportAchievement,
    StudentProfile,
)
from app.models.InternshipPost import (
    PostInternship,

)
admin.site.register(StudentReport)
admin.site.register(StudentReportSkill)
admin.site.register(StudentReportAchievement)
admin.site.register(StudentProfile)
admin.site.register(PostInternship)
# admin.site.register(StudentApplication)
# admin.site.register(BrowsePostsInternships)



