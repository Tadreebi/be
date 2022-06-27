# Generated by Django 4.0.5 on 2022-06-26 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_remove_postinternship_num_of_applications_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentApplications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('resume', models.ImageField(blank=True, upload_to='resumes_images')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('internship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.postinternship')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]