# Generated by Django 4.0.5 on 2022-06-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_studentapplications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentapplications',
            old_name='name',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='studentapplications',
            name='expected_salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentapplications',
            name='suitable_working_hours',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Remote', 'Remote')], default='Part Time', max_length=50),
        ),
        migrations.AddField(
            model_name='studentapplications',
            name='what_can_you_bring_to_the_company',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
