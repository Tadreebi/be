from django.db import models
from .Users import StudentUser

RATING_MARKS = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


class UniStuFeedback(models.Model):

    student = models.ForeignKey(
        StudentUser,
        related_name="student_idUniStuFeedback",
        on_delete=models.CASCADE,
    )
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING_MARKS)

    def __str__(self):
        return self.student.username
