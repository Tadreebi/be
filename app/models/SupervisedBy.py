from django.db import models
from .User import UniversityEmployeeUser, StudentUser, CompanyUser


class SupervisedBy(models.Model):
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, unique=True)
    supervisor = models.ForeignKey(UniversityEmployeeUser, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username