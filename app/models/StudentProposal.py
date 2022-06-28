from pickle import FALSE
from .Users import StudentUser, CompanyUser, UniversityEmployeeUser
from .StudentApplications import StudentApplications
from django.db import models


class StudentUniProposal(models.Model):
    student = models.ForeignKey(
        StudentUser,
        on_delete=models.CASCADE, related_name="student_idStudentUniProposal", default=1
    )
    company = models.ForeignKey(
        CompanyUser, on_delete=models.CASCADE, related_name="company_idStudentUniProposal", default=1
    )
    internship_application = models.ForeignKey(
        StudentApplications, on_delete=models.CASCADE, related_name="post_idStudentUniProposal", default=1
    )  # Double check of default neccssaty
    # Uni Supervisor notes
    remarks = models.TextField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.username
