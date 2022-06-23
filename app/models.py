from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from phonenumber_field.modelfields import PhoneNumberField


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class AppUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name="ID number (univesity ID)", max_length=64, unique=True
    )
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # editable=False

    CITIES = [
        ("Amman", "Amman"),
        ("Aqaba", "Aqaba"),
        ("Irbid", "Irbid"),
        ("Jarash", "Jarash"),
        ("Mafraq", "Mafraq"),
        ("Madaba", "Madaba"),
        ("Zarqa", "Zarqa"),
        ("Tafilah", "Tafilah"),
        ("Salt", "Salt"),
        ("Maan", "Maan"),
        ("Karak", "Karak"),
        ("Ajloun", "Ajloun"),
    ]

    MAJORS = [
        ("IT", "IT"),
        ("Engineering", "Engineering"),
        ("Science", "Science"),
        ("Business", "Business"),
        ("Medicine", "Medicine"),
        ("Law", "Law"),
        ("Letreture", "Letreture"),
    ]

    email = models.EmailField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    phone = PhoneNumberField(unique=True, null=True, blank=True)
    address = models.CharField(
        help_text="city", max_length=32, choices=CITIES, null=True, blank=True
    )
    GPA = models.DecimalField(
        help_text="out of 4.00", max_digits=4, decimal_places=2, null=True, blank=True
    )
    major = models.CharField(max_length=32, choices=MAJORS, null=True, blank=True)

    objects = MyUserManager()

    # to specify which field is used for login
    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = [
        "email",
    ]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
