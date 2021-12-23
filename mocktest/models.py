from django.db import models
from app.models import Category
from django.core.validators import MaxValueValidator,MinValueValidator
from users.models import User

Difficulty_Choice=(
    ('easy','easy'),
    ('medium','medium'),
    ('high','high')
)
class MockTest(models.Model):
    title=models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    difficulty=models.CharField(choices=Difficulty_Choice,max_length=50)
    description=models.TextField(blank=True,null=True)
    price=models.IntegerField(default=0)

    @property
    def no_of_ratings(self):
        ratings=MockTestRating.objects.filter(mocktest=self)
        return len(ratings)

    @property
    def mocktest_rating(self):
        sum=0
        ratings=MockTestRating.objects.filter(mocktest=self)
        for rating in ratings:
            sum+=rating.stars
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

    @property
    def total_participants(self):
        tt=MyMockTest.objects.filter(mocktest=self)
        return len(tt)

    @property
    def total_set(self):
        sets=TestSet.objects.filter(mocktest=self)
        return len(sets)

    @property
    def total_qstn(self):
        qstns=TestQuestion.objects.filter(mocktest=self)
        return len(qstns)

class MockTestRating(models.Model):
    mocktest=models.ForeignKey(MockTest,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.TextField(blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    class Meta:
        unique_together=(('user','mocktest'),)
        index_together=(('user','mocktest'),)

class MyMockTest(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mocktest=models.ForeignKey(MockTest,on_delete=models.CASCADE)
    




class TestSet(models.Model):
    mocktest=models.ForeignKey(MockTest,on_delete=models.CASCADE)
    position=models.IntegerField()

    @property
    def total_ques(self):
        tq=TestQuestion.objects.filter(testset=self)
        return len(tq)

    def __str__(self):
        
        return self.mocktest.title+str(self.id)

class TestQuestion(models.Model):
    mocktest=models.ForeignKey(MockTest,on_delete=models.CASCADE)
    testset=models.ForeignKey(TestSet,on_delete=models.CASCADE)
    question=models.CharField(max_length=255)
    option1=models.CharField(max_length=255)
    option2=models.CharField(max_length=255)
    option3=models.CharField(max_length=255)
    option4=models.CharField(max_length=255)
    correct=models.CharField(max_length=255)
    solution=models.CharField(max_length=500,blank=True,null=True)

class MyTestSet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    testset=models.ForeignKey(TestSet,on_delete=models.CASCADE)
    is_completed=models.BooleanField(default=True)
    total_mark=models.IntegerField()

class UserTest(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    testset=models.ForeignKey(TestSet,on_delete=models.CASCADE)
    question=models.ForeignKey(TestQuestion,on_delete=models.CASCADE)
    answer=models.CharField(max_length=255,blank=True,null=True)

class TestWishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    test=models.ForeignKey(MockTest,on_delete=models.CASCADE)

    def __str__(self):
        return self.MockTest.title

class TestCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    test=models.ForeignKey(MockTest,on_delete=models.CASCADE)

    def __str__(self):
        return self.MockTest.title