from .Users import StudentUser, CompanyUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ComapnyRating(models.Model):
    student = models.ForeignKey(
        StudentUser,
        on_delete=models.CASCADE,
        unique=True,
        blank=True,
        null=True,
        related_name="student_id",
    )
    company = models.ForeignKey(
        CompanyUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="company_id",
    )

    score = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
    )

    useful_train = models.SmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
        default=5,
    )
    student_allowed = models.SmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
        default=5,
    )
    support = models.SmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
        default=5,
    )
    recomended = models.SmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
        default=5,
    )
    comments = models.TextField(max_length=480, blank=True, null=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company.username
