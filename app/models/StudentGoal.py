from django.contrib.auth import get_user_model
from django.db import models
from .User import StudentUser, AppUser


class StudentGoal(models.Model):
    title = models.CharField(max_length=256)
    student = models.ForeignKey(
        StudentUser, related_name="student_idStudentGoal", on_delete=models.CASCADE
    )
    describtion = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author = models.ForeignKey(
    #     AppUser,
    #     on_delete=models.CASCADE,
    #     editable=False,
    #     null=True,
    #     blank=True,
    # )

    def __str__(self):
        return self.title


class StudentGoalIndicator(models.Model):
    title = models.CharField(max_length=256)
    goal = models.ForeignKey(StudentGoal, on_delete=models.CASCADE)
    describtion = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author = models.ForeignKey(
    #     AppUser,
    #     on_delete=models.CASCADE,
    #     editable=False,
    #     null=True,
    #     blank=True,
    # )

    def __str__(self):
        return self.title
