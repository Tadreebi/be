from datetime import *
from django.db import models
from location_field.models.plain import PlainLocationField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from .User import StudentUser, CompanyUser, AppUser


class InternshipType(models.TextChoices):
    Full_Time = "Full Time"
    Part_Time = "Part Time"


class Location(models.TextChoices):
    On_Site = "On Site"
    Remote = "Remote"


class Education(models.TextChoices):
    Bachelors = "BACHELORS"
    Masters = "MASTERS"
    Phd = "PHD"


class Experience(models.TextChoices):
    No_Experience = "No Experience"
    One_Year = "One Year"
    Two_Years = "Two Years"
    Three_Years_And_Above = "Three Years and Above"


class Industry(models.TextChoices):
    Business = "BUSINESS"
    IT = "IT"
    Banking = "BANKING"
    Education = "EDUCATION"
    Engineering = "ENGINEERING"
    Medical = "MEDICAL"
    Others = "OTHERS"


def return_date_time():
    now = datetime.now()
    return now + timedelta(days=10)


class InternshipPost(models.Model):
    company = models.ForeignKey(
        CompanyUser, on_delete=models.CASCADE, related_name="company_idInternshipPost"
    )
    position = models.CharField(max_length=255, null=True)
    type = models.CharField(
        max_length=50, choices=InternshipType.choices, default=InternshipType.Full_Time
    )
    location = models.CharField(
        max_length=50, choices=Location.choices, default=Location.On_Site
    )
    education = models.CharField(
        max_length=50, choices=Education.choices, default=Education.Bachelors
    )
    industry = models.CharField(
        max_length=50, choices=Industry.choices, default=Industry.Business
    )
    # To pick industry out of uni faculties / majors
    # industry = models.ForeignKey(
    #     MajorOrFaculty, on_delete=models.CASCADE, related_name="company_id"
    # )
    experience = models.CharField(
        max_length=50, choices=Experience.choices, default=Experience.No_Experience
    )
    paid = models.BooleanField(default=False)
    salary = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    city = models.CharField(max_length=255, null=True)
    location = PlainLocationField(based_fields=["city"], zoom=7, null=True)
    vacancies = models.IntegerField(default=1)
    description = models.TextField(max_length=500, null=True)
    # Company Supervisor Data
    supervisor_Name = models.CharField(max_length=256)
    supervisor_phone_number = models.CharField(max_length=256)
    subervisor_position = models.CharField(max_length=256)
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
        return f"{self.position} - {self.company.name}"
