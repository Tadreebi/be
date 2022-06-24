from django.contrib.auth import get_user_model
from django.db import models

choices = ["Weekly", "Monthly", "Final"]


class StudentReports(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    type = models.CharField(choices=choices)
    # Start & end of period covered by the report
    startDate = models.DateField()
    endDate = models.DateField()
    # Report intro & conclusion paragraphs
    intro = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class StudentReportSkills(models.Model):
    title = models.CharField(max_length=256)
    report = models.ForeignKey(StudentReports, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    # For student profile customization (to decide is this is to include in the profile)
    profile = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class StudentReportAchievements(models.Model):
    title = models.CharField(max_length=256)
    report = models.ForeignKey(StudentReports, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    # For student profile customization (to decide is this is to include in the profile)
    profile = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
