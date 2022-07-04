from .User import StudentUser, CompanyUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .User import AppUser


class CompanyRating(models.Model):
    student = models.ForeignKey(
        StudentUser,
        on_delete=models.CASCADE,
        unique=True,
        blank=True,
        null=True,
        related_name="student_idCompanyRating",
    )
    company = models.ForeignKey(
        CompanyUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="company_idCompanyRating",
    )
    """
    This is a calculated score that will represent the company rating 
    """
    score = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
    )
    """
    # These are the question the company rating score will rely on, The student will answer each
     questions out of 10 points :
    """

    """
    1. Does the training program covers it's description?
    """

    useful_train = models.SmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
        default=5,
    )
    """
    2. you were allowed to use the tools and technology of the company 
    with during the training program? 
    """

    student_allowed = models.SmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
        default=5,
    )
    """
    3. Did you find sufficient help and support when needed?
    """
    support = models.SmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
        default=5,
    )

    """
     4.Out of 10, How you would rate your improvement during the training course? 
    """
    improvement = models.SmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
        default=5,
    )

    """
    5. Do you recommend this training program for other students?
    """
    recomended = models.SmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
        default=5,
    )

    """
    Additional reviews and suggestions  :
    """
    comments = models.TextField(max_length=480, blank=True, null=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.company.username
