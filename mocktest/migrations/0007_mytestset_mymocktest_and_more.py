# Generated by Django 4.0.1 on 2022-01-10 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mocktest', '0006_alter_usertest_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytestset',
            name='mymocktest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mocktest.mymocktest'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='mymocktest',
            unique_together={('user', 'mocktest')},
        ),
        migrations.AlterIndexTogether(
            name='mymocktest',
            index_together={('user', 'mocktest')},
        ),
    ]
