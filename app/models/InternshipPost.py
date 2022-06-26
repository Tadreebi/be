from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class InternshipType(models.TextChoices):
    Full_Time = 'Full Time'
    Part_Time = 'Part Time'
    Remote = 'Remote'

class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    Phd = 'Phd'

class Experience(models.TextChoices):
    No_Experience = 'No Experience'
    One_Year = 'One Year'
    Two_Years = 'Two Years'
    Three_Years_And_Above = 'Three Years and Above'

class Industry(models.TextChoices):
    Business = 'Business'
    IT = 'IT'
    Banking = 'Banking'
    Education = 'Education'
    Engineering = 'Engineering'
    Medical = 'Medical'
    Others = 'Others'

class InternshipSalary(models.TextChoices):
    Paid = 'Paid'
    UnPaid = 'UnPaid Internship'

class PostInternship(models.Model):
    company_name = models.CharField(max_length=150, null=True)
    title = models.CharField(max_length=255, null=True)
    position = models.TextField()
    description = models.TextField(max_length=500, null=True)
    min_requirements = models.TextField(max_length=500, null=True)
    email = models.EmailField(null=True)
    schedule = models.CharField(
        max_length=50,
        choices=InternshipType.choices,
        default=InternshipType.Full_Time
    )
    education = models.CharField(
        max_length=50,
        choices=Education.choices,
        default=Education.Bachelors
    )
    industry= models.CharField(
        max_length=50,
        choices=Industry.choices,
        default=Industry.Business
    )
    experience= models.CharField(
        max_length=50,
        choices=Experience.choices,
        default=Experience.No_Experience
    )
    internshipType= models.CharField(
        max_length=50,
        choices=InternshipSalary.choices,
        default=InternshipSalary.UnPaid
    )

    salary = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10000000)])
    location = models.TextField(max_length=255, null=True)
    positions = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now_add=False, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

