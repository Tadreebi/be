from django.db import models


class FacultiesChoices(models.TextChoices):
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


# keep those choices and give the ability to add more #################################
