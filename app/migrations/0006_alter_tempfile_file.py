# Generated by Django 4.0.1 on 2022-01-13 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_tempfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempfile',
            name='file',
            field=models.FileField(upload_to='videos'),
        ),
    ]
