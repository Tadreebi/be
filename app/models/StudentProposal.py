from pickle import FALSE
from .Users import StudentUser, CompanyUser, UniversityEmployeeUser
from django.db import models


class StudentUniProposal(models.Model):
    student = models.ForeignKey(
        StudentUser, on_delete=models.CASCADE, related_name="student_id", default=1
    )
    company = models.ForeignKey(
        CompanyUser, on_delete=models.CASCADE, related_name="company_id", default=1
    )  # DOuble check of default neccssaty
    # Move supervisor data to opeertunity post data ##################
    supervisor_Name = models.CharField(max_length=256)
    supervisor_phone_number = models.CharField(max_length=256)
    subervisor_position = models.CharField(max_length=256)
    # ForeignKey to student application to oppertunity ##################
    # Supervisor notes
    remarks = models.TextField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_Name
