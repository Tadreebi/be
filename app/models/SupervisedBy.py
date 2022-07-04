from django.db import models
from .User import UniversityEmployeeUser, StudentUser, CompanyUser


class SupervisedBy(models.Model):
    student = models.OneToOneField(StudentUser, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(UniversityEmployeeUser, on_delete=models.CASCADE)
    company = models.ForeignKey(
        CompanyUser, on_delete=models.CASCADE, null=True, blank=True
    )
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.username
