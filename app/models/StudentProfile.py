from django.db import models
from .User import StudentUser, AppUser
from django.core.validators import MaxValueValidator, MinValueValidator


class StudentProfile(models.Model):
    student = models.ForeignKey(
        StudentUser, related_name="student_idStudentProfile", on_delete=models.CASCADE
    )
    intro = models.TextField(null=True, blank=True)
    image = models.ImageField(blank=True, upload_to="profile_images", null=True)
    job_title = models.CharField(max_length=256, null=True, blank=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.student.username


class StudentProfileExperience(models.Model):
    profile = models.ForeignKey(
        StudentProfile,
        related_name="profile_idStudentProfileExperience",
        on_delete=models.CASCADE,
    )
    title = models.TextField(max_length=256)
    details = models.CharField(max_length=256, null=True, blank=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class StudentProfileSkill(models.Model):
    profile = models.ForeignKey(
        StudentProfile,
        related_name="profile_idStudentProfileSkill",
        on_delete=models.CASCADE,
    )
    title = models.TextField(max_length=256)
    details = models.CharField(max_length=256, null=True, blank=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class StudentProfileEducation(models.Model):
    profile = models.ForeignKey(
        StudentProfile,
        related_name="profile_idStudentProfileEducation",
        on_delete=models.CASCADE,
    )
    title = models.TextField(max_length=256)
    details = models.CharField(max_length=256, null=True, blank=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class StudentProfileLanguage(models.Model):
    profile = models.ForeignKey(
        StudentProfile,
        related_name="profile_idStudentProfileLanguage",
        on_delete=models.CASCADE,
    )
    title = models.TextField(max_length=256)
    level = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    details = models.CharField(max_length=256, null=True, blank=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class StudentProfileContact(models.Model):
    profile = models.ForeignKey(
        StudentProfile,
        related_name="profile_idStudentProfileContacts",
        on_delete=models.CASCADE,
    )
    title = models.TextField(max_length=256)
    link = models.CharField(max_length=256, null=True, blank=True)
    details = models.CharField(max_length=256, null=True, blank=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class StudentProfileWork(models.Model):
    profile = models.ForeignKey(
        StudentProfile,
        related_name="profile_idStudentProfileWork",
        on_delete=models.CASCADE,
    )
    title = models.TextField(max_length=256)
    image = models.ImageField(
        blank=True,
        upload_to="works",
        null=True,
    )
    link = models.CharField(max_length=256, null=True, blank=True)
    details = models.CharField(max_length=256, null=True, blank=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
