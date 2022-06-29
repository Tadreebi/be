from django.db import models


class FacultyChoices(models.TextChoices):
    not_a_student = "Not a Student", "Not a Student"
    it = "IT", "IT"
    engineering = "Engineering", "Engineering"
    science = "Science", "Science"
    business = "Business", "Business"
    medicine = "Medicine", "Medicine"
    nursing = "Nursing", "Nursing"
    pharmacy = "Pharmacy", "Pharmacy"
    law = "Law", "Law"
    letreture = "Letreture", "Letreture"
    arts = "Arts", "Arts"
    humanities = "Humanities", "Humanities"
    religions = "Religions", "Religions"


# MONTHS = [(1, 1), (3, 3), (6, 6), (9, 9), (12, 12), ("more", "more")]


# class Faculty(models.Model):
#     faculty_name = models.CharField(max_length=50)
#     training_duration = models.CharField(
#         help_text="months", max_length=10, choices=MONTHS
#     )

#     def __str__(self):
#         return self.faculty
