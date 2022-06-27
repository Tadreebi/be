from django.db import models
from django.contrib.auth import get_user_model

class Report(models.Model):

    RATING_MARKS = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

    # student_username = models.ForeignKey(
    #     "StudentUser",
    #     verbose_name="Student ID (University ID)",
    #     on_delete=models.CASCADE,
    # )
    report = models.TextField()
    report_number=models.ForeignKey(get_user_model(), on_delete=models.CASCADE, unique=True, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    mark = models.IntegerField(choices=RATING_MARKS)
    training_duration=models.IntegerField(max_length=12)



    def __str__(self):
        return self.student_username.username