from django.db import models
from .Users import AppUser

choices = [("Weekly", "Weekly"), ("Monthly", "Monthly"), ("Final", "Final")]


class StudentReport(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    student = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=256, choices=choices)
    # Start & end of period covered by the report
    startDate = models.DateField()
    endDate = models.DateField()
    # Report intro & conclusion paragraphs
    intro = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    # Supervisor notes
    remarks = models.TextField(null=True, blank=True)
    accepted = models.BooleanField(default=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class StudentReportSkill(models.Model):
    title = models.CharField(max_length=256)
    report = models.ForeignKey(StudentReport, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    # For student profile customization (to decide is this is to include in the profile)
    profile = models.BooleanField(default=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class StudentReportAchievement(models.Model):
    title = models.CharField(max_length=256)
    report = models.ForeignKey(StudentReport, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    # For student profile customization (to decide is this is to include in the profile)
    profile = models.BooleanField(default=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
