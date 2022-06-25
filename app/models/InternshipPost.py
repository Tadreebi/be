from django.db import models

class PostInternship(models.Model):
    title = models.CharField(max_length=255)
    position = models.TextField()
    description = models.TextField()
    schedule = models.TextField()
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    num_of_applications = models.IntegerField(default=0)

# class StudentApplication(models.Model):
#     name = models.CharField(max_length=255)
#     title = models.ForeignKey(PostInternship, related_name="application", on_delete=models.CASCADE)
#     position = models.ForeignKey(PostInternship, related_name="application", on_delete=models.CASCADE)

# class BrowsePostsInternships(models.Model):
#     posts = models.ForeignKey(PostInternship, related_name="intership-posts", on_delete=models.CASCADE)