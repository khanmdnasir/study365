from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display=['id','name']
    def name(self,obj):
        link=reverse("admin:tutor_instructor_change", args=[obj.user.pk])
        return format_html('<a href="{}">{}</a>',link,obj.user.username)