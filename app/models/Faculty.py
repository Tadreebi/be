from django.db import models


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=128)
    major = models.CharField(max_length=128)
    training_duration = models.IntegerField(help_text="months")
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.faculty_name + " - " + self.major
