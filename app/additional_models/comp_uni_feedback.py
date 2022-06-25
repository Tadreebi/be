from django.db import models


class CompUniFeedback(models.Model):

    RATING_MARKS = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

    student_username = models.ForeignKey(
        "StudentUser",
        verbose_name="Student ID (University ID)",
        on_delete=models.CASCADE,
    )
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING_MARKS)

    def __str__(self):
        return self.student_username + " " + self.rating
