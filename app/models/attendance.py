from django.contrib.auth import get_user_model
from django.db import models




class Attendance(models.Model):
    full_name = models.CharField(max_length=256, null=True, blank=True)
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, unique=True)
   
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
