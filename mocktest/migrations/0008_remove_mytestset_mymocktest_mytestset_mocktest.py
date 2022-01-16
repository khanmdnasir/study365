# Generated by Django 4.0.1 on 2022-01-10 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mocktest', '0007_mytestset_mymocktest_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytestset',
            name='mymocktest',
        ),
        migrations.AddField(
            model_name='mytestset',
            name='mocktest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mocktest.mocktest'),
            preserve_default=False,
        ),
    ]