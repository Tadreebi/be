from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Rating(models.Model):
   
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]



    )

    company_name =models.CharField(max_length=64, default="")
    useful_train=models.SmallIntegerField(max_length=10, default= 5)
    student_allowed=models.SmallIntegerField(max_length=10, default= 5)
    support=models.SmallIntegerField(max_length=10, default= 5)
    recomended=models.SmallIntegerField(max_length=10, default= 5)
    comments=models.TextField(max_length=480,blank=True, null=True)
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, unique=True, blank=True, null=True)



    def __str__(self):
        return str(self.pk)

