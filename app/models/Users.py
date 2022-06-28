from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from .Faculties import FacultiesChoices


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError("Users must have an email address")

        if not username:
            raise ValueError("Users must have a username")

        if not password:
            raise ValueError("Users must have a password")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=make_password(password),
        )
        # user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=make_password(password),
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.type = "University Employee"
        user.save(using=self._db)
        return user


class StudentManager(MyUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=AppUser.Types.student)


class UneversityEmployManager(MyUserManager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(type=AppUser.Types.university_employee)
        )


class CompanyManager(MyUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=AppUser.Types.company)


class UserNameField(models.SlugField):
    def __init__(self, *args, **kwargs):
        super(UserNameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class AppUser(AbstractBaseUser):
    class Types(models.TextChoices):
        student = "STUDENT", "Student"
        university_employee = "University Employee", "University Employee"
        company = "COMPANY", "Company"

    objects = MyUserManager()

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

    # MAJORS = [
    #     ("Not a Student", "Not a Student"),
    #     ("IT", "IT"),
    #     ("Engineering", "Engineering"),
    #     ("Science", "Science"),
    #     ("Business", "Business"),
    #     ("Medicine", "Medicine"),
    #     ("Law", "Law"),
    #     ("Letreture", "Letreture"),
    # ]
    # Split to own model, and include required internship duration (faculty not major)

    username = UserNameField(
        help_text="If you are a (student/university Employee) use the university ID number. If you are a company use the comapany name and replace the spaces with dash (-)",
        max_length=64,
        unique=True,
    )
    email = models.EmailField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    # first_name = models.CharField(max_length=64, null=True, blank=True)
    # last_name = models.CharField(max_length=64, null=True, blank=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    type = models.CharField(
        ("Type"), max_length=50, choices=Types.choices, default=Types.student
    )
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_superuser = models.BooleanField(default=False, editable=False)
    is_active = models.BooleanField(default=True, editable=False)
    is_admin = models.BooleanField(default=False, editable=False)
    is_staff = models.BooleanField(default=False, editable=False)
    phone = PhoneNumberField(
        unique=True, help_text="+962*********", null=True, blank=True
    )
    address = models.CharField(
        help_text="city", max_length=32, choices=CITIES, null=True, blank=True
    )
    GPA = models.DecimalField(
        help_text="out of 4.00, If You are not a student leave it",
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
    )
    faculty = models.CharField(
        ("Faculties"),
        max_length=64,
        choices=FacultiesChoices.choices,
        default=FacultiesChoices.not_a_student,
    )
    # major = models.CharField(
    #     max_length=32, choices=MAJORS, default="Not a Student", null=True, blank=True
    # )
    about = models.TextField(default=None, null=True, blank=True)

    # to specify which field is used for login
    USERNAME_FIELD = "username"

    # additional required fields (username, password)
    REQUIRED_FIELDS = [
        "email",
    ]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class StudentUser(AppUser):
    objects = StudentManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        # self.password = make_password(self.password)
        self.type = AppUser.Types.student
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"slug": self.username})


class UniversityEmployeeUser(AppUser):
    objects = UneversityEmployManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        # self.password = make_password(self.password)
        self.type = AppUser.Types.university_employee
        self.is_staff = True
        self.is_admin = True
        self.major = "Not a Student"
        self.GPA = None
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("university_detail", kwargs={"slug": self.username})


class CompanyUser(AppUser):
    # Add company intro / description as an optional field / key
    objects = CompanyManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        # self.password = make_password(self.password)
        self.type = AppUser.Types.company
        self.major = "Not a Student"
        self.GPA = None
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("company_detail", kwargs={"slug": self.username})
