# Generated by Django 4.0.1 on 2022-01-04 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211223_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='assignment_file',
            field=models.FileField(blank=True, null=True, upload_to='assignment/instructor/'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='studentassignment',
            name='assignment_file',
            field=models.FileField(blank=True, null=True, upload_to='assignment/student/'),
        ),
    ]
