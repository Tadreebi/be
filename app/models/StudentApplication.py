from django.db import models
from django.contrib.auth.models import User
from app.models import InternshipPost
from django.core.validators import RegexValidator
from .User import StudentUser, CompanyUser, AppUser


class InternshipType(models.TextChoices):
    Full_Time = "Full Time"
    Part_Time = "Part Time"


class Location(models.TextChoices):
    On_Site = "On Site"
    Remote = "Remote"


# To be linked with the university table
class University(models.TextChoices):
    University_of_Jordan = "University of Jordan"
    Petra = "Petra"
    American_University_of_Madabah = "American University of Madabah"


class Gpa(models.TextChoices):
    Poor = "Poor"
    Good = "Good"
    Very_Good = "Very Good"
    Excellent = "Excellent"


class StudentApplication(models.Model):
    student = models.ForeignKey(
        StudentUser,
        related_name="student_idStudentApplication",
        on_delete=models.SET_NULL,
        null=True,
    )
    homeFullAddress = models.CharField(max_length=500, null=True)
    internship = models.ForeignKey(InternshipPost, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=50, choices=InternshipType.choices, default=InternshipType.Part_Time
    )
    location = models.CharField(
        max_length=50, choices=Location.choices, default=Location.On_Site
    )
    expected_salary = models.IntegerField(default=0)
    coverletter = models.TextField(max_length=1400, null=True)
    resume = models.FileField(blank=True, upload_to="resumes")

    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.student.username


class StudentApplicationResponse(models.Model):
    application = models.OneToOneField(
        StudentApplication, on_delete=models.CASCADE, unique=True
    )
    remarks = models.CharField(max_length=1000)
    accepted = models.BooleanField(default=False)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )
