from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name']

class QuizAdmin(admin.TabularInline):
    model=Quiz

class LessonAdmin(admin.TabularInline):
    model=Lesson
    

class ChapterAdmin(admin.TabularInline):
    model=Chapter
    


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display=['id','course_title','category_info','instructor_info','course_price']
    summernote_fields=('course_description',)
    inlines=[ChapterAdmin,LessonAdmin,QuizAdmin]
    search_fields=('course_title',)
    def instructor_info(self,obj):
        link=reverse("admin:app_course_change", args=[obj.instructor_id.pk])
        return format_html('<a href="{}">{}</a>',link,obj.instructor_id.user.username)

    def category_info(self,obj):
        link=reverse("admin:app_course_change", args=[obj.course_category.pk])
        return format_html('<a href="{}">{}</a>',link,obj.course_category.category_name)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['id','author_name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['id','book_title']

# admin.site.register(CourseWishList)
# admin.site.register(CourseCart)
# admin.site.register(BookWishList)
# admin.site.register(BookCart)
# admin.site.register(MyCourse)
# admin.site.register(MyBooks)



    
