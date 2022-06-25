# Generated by Django 4.0.4 on 2022-06-25 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AppUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "username",
                    models.CharField(
                        help_text="If you are a (student/university Employee) use the university ID number",
                        max_length=64,
                        unique=True,
                    ),
                ),
                ("email", models.EmailField(max_length=64, unique=True)),
                ("first_name", models.CharField(blank=True, max_length=64, null=True)),
                ("last_name", models.CharField(blank=True, max_length=64, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("STUDENT", "Student"),
                            ("UNIVERSITY_EMPLOYEE", "University Employee"),
                            ("COMPANY", "Company"),
                        ],
                        default="STUDENT",
                        max_length=50,
                        verbose_name="Type",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="date joined"),
                ),
                (
                    "last_login",
                    models.DateTimeField(auto_now=True, verbose_name="last login"),
                ),
                ("is_superuser", models.BooleanField(default=False, editable=False)),
                ("is_active", models.BooleanField(default=True, editable=False)),
                ("is_admin", models.BooleanField(default=False, editable=False)),
                ("is_staff", models.BooleanField(default=False, editable=False)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None, unique=True
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        choices=[
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
                        ],
                        help_text="city",
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "GPA",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="out of 4.00, If You are not a student leave it",
                        max_digits=4,
                        null=True,
                    ),
                ),
                (
                    "major",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("NOT_A_STUDENT", "Not a Student"),
                            ("IT", "IT"),
                            ("Engineering", "Engineering"),
                            ("Science", "Science"),
                            ("Business", "Business"),
                            ("Medicine", "Medicine"),
                            ("Law", "Law"),
                            ("Letreture", "Letreture"),
                        ],
                        default="NOT_A_STUDENT",
                        max_length=32,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="StudentReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Weekly", "Weekly"),
                            ("Monthly", "Monthly"),
                            ("Final", "Final"),
                        ],
                        max_length=256,
                    ),
                ),
                ("startDate", models.DateField()),
                ("endDate", models.DateField()),
                ("intro", models.TextField(blank=True, null=True)),
                ("conclusion", models.TextField(blank=True, null=True)),
                ("remarks", models.TextField(blank=True, null=True)),
                ("accepted", models.BooleanField(default=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentReportSkill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                ("details", models.TextField(blank=True, null=True)),
                ("profile", models.BooleanField(default=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.studentreport",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentReportAchievement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                ("details", models.TextField(blank=True, null=True)),
                ("profile", models.BooleanField(default=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.studentreport",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(blank=True, max_length=256, null=True)),
                ("intro", models.TextField(blank=True, null=True)),
                ("image", models.CharField(blank=True, max_length=256, null=True)),
                ("job_title", models.CharField(blank=True, max_length=256, null=True)),
                ("experiences", models.JSONField(blank=True, default=[])),
                ("skills", models.JSONField(blank=True, default=[])),
                ("educations", models.JSONField(blank=True, default=[])),
                ("languages", models.JSONField(blank=True, default=[])),
                (
                    "contacts",
                    models.JSONField(
                        blank=True,
                        default={
                            "email": "",
                            "facebook": "",
                            "instagram": "",
                            "linkedin": "",
                            "more": {},
                            "phone_no": "",
                            "telegram": "",
                            "twitter": "",
                            "website": "",
                            "whatsapp": "",
                        },
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CompanyUser",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app.appuser",),
        ),
        migrations.CreateModel(
            name="StudentUser",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app.appuser",),
        ),
        migrations.CreateModel(
            name="UniversityEmployeeUser",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app.appuser",),
        ),
    ]
