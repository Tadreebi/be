from django.db import models
from app.models import StudentUser

RATING_MARKS = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

TYPES = [
    ("PERIODICAL_REPORT", "periodical report"),
    ("COMPLAIN", "Complain"),
]


class CompUniFeedback(models.Model):

    student = models.ForeignKey(
        "StudentUser",
        verbose_name="Student ID (University ID)",
        on_delete=models.CASCADE,
    )
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING_MARKS)
    type = models.CharField(max_length=64, default="PERIODICAL_REPORT", choices=TYPES)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.username
