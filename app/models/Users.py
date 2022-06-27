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
        user.type = "university_employee"
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


class AppUser(AbstractBaseUser):
    class Types(models.TextChoices):
        student = "STUDENT", "Student"
        university_employee = "UNIVERSITY_EMPLOYEE", "University Employee"
        company = "COMPANY", "Company"

    objects = MyUserManager()


class AppUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name="ID number (univesity ID)", max_length=64, unique=True
    )
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False, editable=False)
    is_active = models.BooleanField(default=True, editable=False)
    is_staff = models.BooleanField(verbose_name="University staff", default=False)
    is_superuser = models.BooleanField(default=False, editable=False)

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
        ("NOT_A_STUDENT", "Not a Student"),
        ("IT", "IT"),
        ("Engineering", "Engineering"),
        ("Science", "Science"),
        ("Business", "Business"),
        ("Medicine", "Medicine"),
        ("Law", "Law"),
        ("Letreture", "Letreture"),
    ]

    username = models.CharField(
        help_text="If you are a (student/university Employee) use the university ID number",
        max_length=64,
        unique=True,
    )
    email = models.EmailField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    type = models.CharField(
        ("Type"), max_length=50, choices=Types.choices, default=Types.student
    )
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_superuser = models.BooleanField(default=False, editable=False)
    is_active = models.BooleanField(default=True, editable=False)
    is_admin = models.BooleanField(default=False, editable=False)
    is_staff = models.BooleanField(default=False, editable=False)
    is_company = models.BooleanField(verbose_name="Company account", default=False)
    email = models.EmailField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    phone = PhoneNumberField(unique=True, null=True, blank=True)
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
    major = models.CharField(
        max_length=32, choices=MAJORS, default="NOT_A_STUDENT", null=True, blank=True
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


class StudentUser(AppUser):
    objects = StudentManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.type = AppUser.Types.student
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class UniversityEmployeeUser(AppUser):
    objects = UneversityEmployManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.type = AppUser.Types.university_employee
        self.is_staff = True
        self.is_admin = True
        self.major = "NOT_A_STUDENT"
        self.GPA = None
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class CompanyUser(AppUser):
    objects = CompanyManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.type = AppUser.Types.company
        self.major = "NOT_A_STUDENT"
        self.GPA = None
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username