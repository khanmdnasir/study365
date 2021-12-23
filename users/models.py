from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.sites.models import Site
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class User(AbstractUser):
    profile_image=models.ImageField(upload_to='profile_images',blank=True,null=True)
    nid_image=models.ImageField(upload_to='nid_images',blank=True,null=True)
    phone_number = PhoneNumberField(unique=True,blank=True,null=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    is_teacher=models.BooleanField(default=False)
    is_email_verified=models.BooleanField(default=False)
    is_phone_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=4,blank=True,null=True)

Level_Choices=(
    ('c1','One'),
    ('c2','Two'),
    ('c3','Three')
)
Department_Choices=(
    ('s','Science'),
    ('a','Arts'),
    ('c','Commerce'),
    ('g','General')
)
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    education_level=models.CharField(max_length=20,choices=Level_Choices,blank=True,null=True)
    department=models.CharField(max_length=50,choices=Department_Choices,blank=True,null=True)
    about=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.user.username
    
    
    
        
        
    
