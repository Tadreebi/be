from django.contrib.auth import get_user_model
from django.db import models


class StudentGoal(models.Model):
    title = models.CharField(max_length=256)
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    describtion = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)

    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class StudentGoalIndicator(models.Model):
    title = models.CharField(max_length=256)
    goal = models.ForeignKey(StudentGoal, on_delete=models.CASCADE)
    describtion = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)

    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
