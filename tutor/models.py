from django.db import models
from users.models import User
from django.contrib.postgres.fields import ArrayField

class Instructor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    speciality=ArrayField(models.CharField(max_length=50),blank=True,null=True)
    instructor_intro=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.user.username



