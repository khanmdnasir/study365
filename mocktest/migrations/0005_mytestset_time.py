# Generated by Django 4.0.1 on 2022-01-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mocktest', '0004_alter_usertest_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytestset',
            name='time',
            field=models.IntegerField(default=30),
        ),
    ]
