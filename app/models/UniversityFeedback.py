from django.db import models
from .User import StudentUser
from .StudentReport import StudentReport

RATING_MARKS = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


class UniversityFeedback(models.Model):

    student = models.ForeignKey(
        StudentUser,
        related_name="student_idUniversityFeedback",
        on_delete=models.CASCADE,
    )
    report = models.ForeignKey(
        StudentReport,
        related_name="report_idStudentReport",
        on_delete=models.CASCADE,
        unique=True,
    )
    title = models.CharField(max_length=256)
    feedback = models.TextField()
    rating = models.IntegerField(choices=RATING_MARKS)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.username
