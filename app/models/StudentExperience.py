from time import time
from django.db import models
from .Users import StudentUser, CompanyUser


class StudentExperience(models.Model):
    student = models.ForeignKey(
        StudentUser, on_delete=models.CASCADE, related_name="student_id"
    )
    company = models.ForeignKey(
        CompanyUser, on_delete=models.CASCADE, related_name="company_id"
    )
    # ForeignKey to student application to oppertunity ##################
    improved_aspects = models.TextField(max_length=5000, null=True, blank=True)
    missed_aspects = models.TextField(max_length=5000, null=True, blank=True)
    get_hired = models.TextField(max_length=5000, null=True, blank=True)
    more = models.TextField(max_length=5000, null=True, blank=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
