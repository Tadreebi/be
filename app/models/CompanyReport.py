from django.db import models
from django.contrib.auth import get_user_model
from .User import StudentUser, CompanyUser
from django.core.validators import MaxValueValidator, MinValueValidator
from .User import AppUser


TYPES = [
    ("Periodical Report", "Periodical Report"),
    ("Final Report", "Final Report"),
    ("Complain Report", "Complain Report"),
]


class CompanyReport(models.Model):
    # Keys of the comany and the student that it intendeds to make a report about
    student = models.ForeignKey(
        StudentUser,
        related_name="student_idCompanyReport",
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        CompanyUser,
        related_name="company_idCompanyReport",
        on_delete=models.CASCADE,
    )

    # Report Title
    title = models.CharField(max_length=256, null=True, blank=True)
    # Report date
    date = models.DateField()
    # Report type, wether it's periodical, complain or final
    type = models.CharField(max_length=64, default="Periodical Report", choices=TYPES)

    # Report intro & conclusion paragraphs
    intro = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.student.username
