from django.contrib.auth import get_user_model
from django.db import models

choices = [("Weekly", "Weekly"), ("Monthly", "Monthly"), ("Final", "Final")]

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


class StudenProfile(models.Model):
    full_name = models.CharField(max_length=256, null=True, blank=True)
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    intro = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=256, null=True, blank=True)
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
        return self.full_name
