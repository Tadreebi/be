from django.db import models
from django.contrib.auth import get_user_model
from .Users import StudentUser, CompanyUser
from django.core.validators import MaxValueValidator, MinValueValidator

TYPES = [
    ("Periodical Report", "Periodical Report"),
    ("Final Report", "Final Report"),
    ("Complain", "Complain"),
]


class CompanyReport(models.Model):
    student = models.ForeignKey(
        StudentUser,
        verbose_name="Student ID (University ID)",
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        CompanyUser,
        verbose_name="Student ID (University ID)",
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=64, default="Periodical Report", choices=TYPES)
    report = models.TextField()
    attendace = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ],
        default=100,
    )

    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.username