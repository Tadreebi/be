from django.db import models

topics = [
    ("Motivational", "Motivational"),
    ("Skill References", "Skill References"),
    ("Interview References", "Interview References"),
]

types = [
    ("File", "File"),
    ("Multimedia", "Multimedia"),
    ("Book", "Book"),
    ("Article", "Article"),
    ("Event", "Event"),
]


class UniversityTip(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    topic = models.CharField(max_length=256, choices=topics)
    type = models.CharField(max_length=256, choices=types)
    details = models.TextField(null=True, blank=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
