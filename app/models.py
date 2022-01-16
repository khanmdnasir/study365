from operator import mod
from django.db import models
from django.db.models.deletion import DO_NOTHING
from users.models import User
from django.contrib.postgres.fields import ArrayField
from tutor.models import Instructor
import os
from django.core.validators import MaxValueValidator,MinValueValidator
import math

# Create your models here.

    

class Category(models.Model):
    category_name=models.CharField(max_length=255)
    is_popular=models.BooleanField(default=False)
    category_image=models.ImageField(upload_to='category_image',blank=True,null=True)
    is_featured=models.BooleanField(default=False)
    def __str__(self):
        return self.category_name
    @property
    def total_course(self):
        course=Course.objects.filter(course_category=self.id)
        return course.count

class Course(models.Model):
    instructor_id=models.ForeignKey(Instructor,on_delete=models.CASCADE)
    course_category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    course_title=models.CharField(max_length=255)
    course_image=models.ImageField(upload_to='course_image')
    course_overview=models.TextField(blank=True,null=True)
    course_year=models.DateField(auto_now_add=True)
    course_language=models.CharField(max_length=255)
    course_price=models.IntegerField(default=0)
    course_offer=models.PositiveIntegerField(default=0)
    course_include=ArrayField(models.CharField(max_length=255),blank=True,null=True)
    course_outcome=ArrayField(models.CharField(max_length=255),blank=True,null=True)
    course_description=models.TextField(blank=True,null=True)
    course_target=ArrayField(models.CharField(max_length=255),blank=True,null=True)
    is_featured=models.BooleanField(default=False)
    is_popular=models.BooleanField(default=False)
    is_inhouse=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_publish=models.BooleanField(default=False)
    course_duration=models.DurationField()
    def __str__(self):
        return self.course_title
    
    @property
    def course_view(self):
        view=MyCourse.objects.filter(course=self)
        return len(view)

    @property
    def no_of_ratings(self):
        ratings=CourseRating.objects.filter(course=self)
        return len(ratings)

    @property
    def coure_rating(self):
        sum=0
        ratings=CourseRating.objects.filter(course=self)
        for rating in ratings:
            sum+=rating.stars
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

    @property
    def discounted_price(self):
        return self.course_price-math.ceil((self.course_price/100)*self.course_offer)
    @property
    def total_lesson(self):
        lessons=Lesson.objects.filter(course_id=self.id)
        return lessons.count

    @property
    def total_class(self):
        total_class=Lesson.objects.filter(course_id=self.id,lesson_type='V')
        return len(total_class)

class Chapter(models.Model):
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    chapter_name=models.CharField(max_length=255)
    chapter_position=models.PositiveIntegerField()
    
    @property
    def total_lesson(self):
        les=Lesson.objects.filter(chapter_id=self.id)
        
        return les.count

LessonType_Choices=(
    ('Q','Quiz'),
    ('V','Video'),
    ('I','Instruction'),
    ('A','Assignment')
)
class Lesson(models.Model):
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    chapter_id=models.ForeignKey(Chapter,on_delete=models.CASCADE)
    lesson_position=models.PositiveIntegerField()
    lesson_title=models.CharField(max_length=255)
    lesson_type=models.CharField(choices=LessonType_Choices,max_length=2)
    lesson_video=models.FileField(upload_to='videos',blank=True,null=True)
    quiz_instruction=models.TextField(blank=True,null=True)
    assignment_total_mark=models.IntegerField(default=0)
    assignment_pass_mark=models.PositiveIntegerField(default=0)
    quiz_time=models.IntegerField(default=0)
    quiz_total_mark=models.IntegerField(default=0)
    quiz_pass_mark=models.PositiveIntegerField(default=0)
    quiz_negative=models.BooleanField(default=False)
    quiz_negative_value=models.IntegerField(default=0)
    text_instruction=models.TextField(blank=True,null=True)
    assignment_instruction=models.TextField(blank=True,null=True)
    assignment_file=models.FileField(upload_to='assignment/instructor/',blank=True,null=True)
    
    def total_quiz(self):
        quiz=Quiz.objects.filter(lesson=self.id)
        return len(quiz)

    def filename(self):
        return os.path.basename(self.assignment_file.name)

    @property
    def quiz_mark(self):
        sq=StudentQuiz.objects.get(lesson=self)
        return sq.quiz_mark
    
    
        
    

class StudentAssignment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    assignment_file=models.FileField(upload_to='assignment/student/',blank=True,null=True)
    submitted_date=models.DateTimeField(auto_now_add=True)
    mark=models.IntegerField(blank=True,null=True)
    is_completed=models.BooleanField(default=True)
    class Meta:
        unique_together=(('user','lesson'),)
        index_together=(('user','lesson'),)

class Quiz(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    quiz_position=models.PositiveIntegerField()
    question=models.CharField(max_length=1000)
    option=ArrayField(models.CharField(max_length=255),blank=True,null=True)
    correct_answer=models.IntegerField(default=0)

class StudentVideo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    is_completed=models.BooleanField(default=True)
    class Meta:
        unique_together=(('user','lesson'),)
        index_together=(('user','lesson'),)

class StudentQuiz(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    quiz_mark=models.IntegerField(default=0)
    is_completed=models.BooleanField(default=True)

    class Meta:
        unique_together=(('user','lesson'),)
        index_together=(('user','lesson'),)
    

class Author(models.Model):
    author_name=models.CharField(max_length=255)
    author_image=models.ImageField(upload_to='authors',blank=True,null=True)
    author_designation=models.CharField(max_length=255,blank=True,null=True)
    author_address=models.CharField(max_length=255,blank=True,null=True)
    author_total_book=models.IntegerField(default=0)
    author_introduction=models.TextField(blank=True,null=True)
    author_email=models.CharField(max_length=255,blank=True,null=True)
    author_contact=models.CharField(max_length=20,blank=True,null=True)
    author_facebook=models.CharField(max_length=255,blank=True,null=True)
    author_twitter=models.CharField(max_length=255,blank=True,null=True)
    author_linkedin=models.CharField(max_length=255,blank=True,null=True)
    
    @property
    def total_books(self):
        books=Book.objects.filter(author_id=self.id)
        return books.count
    def __str__(self):
        return self.author_name

class Book(models.Model):
    author_id=models.ForeignKey(Author,on_delete=models.CASCADE)
    book_image=models.ImageField(upload_to='library')
    book_title=models.CharField(max_length=255)
    
    book_description=models.TextField(blank=True,null=True)
    publishing_year=models.DateField()
    book_language=models.CharField(max_length=255)
    book_price=models.IntegerField(default=0)
    book_offer=models.IntegerField(default=0)
    book_stock=models.IntegerField(default=0)
    book_isbn=models.CharField(max_length=255,blank=True,null=True)
    book_publisher=models.CharField(max_length=255,blank=True,null=True)
    book_category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    book_tag=ArrayField(models.CharField(max_length=255))
    book_featured=models.BooleanField(default=False)
    book_popular=models.BooleanField(default=False)
    book_inhouse=models.BooleanField(default=False)

    def total_sales(self):
        sales=MyBooks.objects.filter(book=self)
        return len(sales)
        
    def no_of_ratings(self):
        ratings=BookRating.objects.filter(book=self)
        return len(ratings)

    def book_review(self):
        sum=0
        ratings=BookRating.objects.filter(book=self)
        for rating in ratings:
            sum+=rating.stars
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

    @property
    def discounted_price(self):
        return self.book_price-((self.book_price/100)*self.book_offer)

    def __str__(self):
        return self.book_title

class CourseRating(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.TextField(blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    class Meta:
        unique_together=(('user','course'),)
        index_together=(('user','course'),)

class BookRating(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.TextField(blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    class Meta:
        unique_together=(('user','book'),)
        index_together=(('user','book'),)

class BookWishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return self.book.book_title
    

class CourseWishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.course.course_title

class CourseCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.course.course_title

class BookCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return self.book.book_title

    @property
    def total_price(self):
        return self.qty*self.book.book_price



class MyCourse(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE)
    def __str__(self):
        return self.course.course_title

Order_Status=(
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)
class MyBooks(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    qty=models.PositiveSmallIntegerField()
    status=models.CharField(max_length=30,choices=Order_Status,default='Pending')
    def __str__(self):
        return self.book.book_title
    


class TempFile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.FileField(upload_to='videos')