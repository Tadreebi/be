from django.db import models
from .User import AppUser

types = [
    ("File", "File"),
    ("Image", "Image"),
    ("Video", "Video"),
    ("Text", "Text"),
    ("Event", "Event"),
]


class UniversityTipTopic(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author = models.ForeignKey(
    #     AppUser,
    #     on_delete=models.CASCADE,
    #     editable=False,
    #     null=True,
    #     blank=True,
    # )

    def __str__(self):
        return self.title


class UniversityTip(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    topic = models.ForeignKey(
        UniversityTipTopic,
        on_delete=models.CASCADE,
        related_name="tip_idUniversityTipTopic",
    )
    type = models.CharField(max_length=256, choices=types)
    details = models.TextField(null=True, blank=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author = models.ForeignKey(
    #     AppUser,
    #     on_delete=models.CASCADE,
    #     editable=False,
    #     null=True,
    #     blank=True,
    # )

    def __str__(self):
        return self.title
