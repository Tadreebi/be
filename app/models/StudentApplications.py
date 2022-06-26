from django.db import models
from django.contrib.auth.models import User
from app.models.InternshipPost import PostInternship
from django.core.validators import RegexValidator

class InternshipType(models.TextChoices):
    Full_Time = 'Full Time'
    Part_Time = 'Part Time'

class Location(models.TextChoices):
    On_Site = 'On Site'
    Remote = 'Remote'

# To be linked with the university table
class University(models.TextChoices):
    University_of_Jordan = 'University of Jordan'
    Petra = 'Petra'
    American_University_of_Madabah = 'American University of Madabah'

class Gpa(models.TextChoices):
    Poor = 'Poor'
    Good = 'Good'
    Very_Good = 'Very Good'
    Excellent = 'Excellent'

class StudentApplications(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=500, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    Address = models.CharField(max_length=500, null=True)
    gpa = models.CharField(
        max_length=50,
        choices=Gpa.choices,
        default=Gpa.Excellent
    )
    university = models.CharField(
        max_length=50,
        choices=University.choices,
        default=University.University_of_Jordan
    )
    internship = models.ForeignKey(PostInternship, on_delete=models.CASCADE)
    suitable_Internship_Type = models.CharField(
        max_length=50,
        choices=InternshipType.choices,
        default=InternshipType.Part_Time
    )
    suitable_location = models.CharField(
        max_length=50,
        choices=Location.choices,
        default=Location.On_Site
    )
    expected_salary = models.IntegerField(default=0)
    what_can_you_bring_to_the_company = models.TextField(max_length=500, null=True)
    resume= models.ImageField(blank=True, upload_to='resumes_images')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.full_name