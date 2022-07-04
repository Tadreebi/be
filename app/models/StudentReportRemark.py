from django.db import models

from .StudentReport import StudentReport
from .User import AppUser


class StudentReportRemark(models.Model):
    report = models.ForeignKey(
        StudentReport,
        related_name="report_idStudentReport",
        on_delete=models.CASCADE,
        unique=True,
    )
    # Supervisor notes
    remarks = models.TextField(null=True, blank=True)
    accepted = models.BooleanField(default=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.report.title
