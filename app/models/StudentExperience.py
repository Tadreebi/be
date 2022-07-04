from time import time
from django.db import models
from .User import StudentUser, CompanyUser


class StudentExperience(models.Model):
    student = models.ForeignKey(
        StudentUser,
        on_delete=models.CASCADE,
        related_name="student_idStudentExperience",
    )
    company = models.ForeignKey(
        CompanyUser,
        on_delete=models.CASCADE,
        related_name="company_idStudentExperience",
    )
    # ForeignKey to student application to oppertunity ##################
    improved_aspects = models.TextField(max_length=5000, null=True, blank=True)
    missed_aspects = models.TextField(max_length=5000, null=True, blank=True)
    get_hired = models.TextField(max_length=5000, null=True, blank=True)
    more = models.TextField(max_length=5000, null=True, blank=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.username
