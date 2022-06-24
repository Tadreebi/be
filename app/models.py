from django.contrib.auth import get_user_model
from django.db import models

choices = ["Weekly", "Monthly", "Final"]


class StudentReports(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    student = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False, blank=False
    )
    type = models.CharField(choices=choices)
    # Start & end of period covered by the report
    startDate = models.DateField()
    endDate = models.DateField()
    # Report intro paragraph
    intro = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
