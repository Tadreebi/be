from django.db import models
from .Users import StudentUser

RATING_MARKS = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

TYPES = [
    ("periodical report", "periodical report"),
    ("Complain", "Complain"),
]


class CompUniFeedback(models.Model):

    student = models.ForeignKey(
        StudentUser,
        related_name="student_idCompUniFeedback",
        on_delete=models.CASCADE,
    )
    feedback = models.TextField()
    rating = models.IntegerField(choices=RATING_MARKS)
    type = models.CharField(max_length=64, default="periodical report", choices=TYPES)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.username
