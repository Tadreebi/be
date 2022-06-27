from django.contrib.auth import get_user_model
from django.db import models


class StudentUniProposal(models.Model):
    full_name = models.CharField(max_length=256)
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, unique=True)
    student_Number= models.CharField(max_length=20)
    company_Name=models.CharField(max_length=64)
    company_adress=models.CharField(max_length=256)
    company_phone_number=models.CharField(max_length=15)
    supervisor_Name=models.CharField(max_length=256)
    supervisor_phone_number=models.CharField(max_length=256)
    subervisor_position=models.CharField(max_length=256)
    submission_date=models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.company_Name







    
