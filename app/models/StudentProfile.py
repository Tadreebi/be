from django.db import models
from .Users import StudentUser

contacts = {
    "website": "",
    "email": "",
    "linkedin": "",
    "facebook": "",
    "instagram": "",
    "twitter": "",
    "phone_no": "",
    "whatsapp": "",
    "telegram": "",
    "more": {},
}


class StudentProfile(models.Model):
    student = models.ForeignKey(
        StudentUser,
        related_name="student_idStudentProfile",
        on_delete=models.CASCADE
    )  # Switch one-to-one
    intro = models.TextField(null=True, blank=True)
    image = models.ImageField(blank=True, upload_to="students_picture", null=True)
    job_title = models.CharField(max_length=256, null=True, blank=True)
    experiences = models.JSONField(default=[], blank=True)
    skills = models.JSONField(default=[], blank=True)
    educations = models.JSONField(default=[], blank=True)
    languages = models.JSONField(default=[], blank=True)
    contacts = models.JSONField(default=contacts, blank=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.username
