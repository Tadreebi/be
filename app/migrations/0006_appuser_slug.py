# Generated by Django 4.0.5 on 2022-06-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_compunifeedback_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]