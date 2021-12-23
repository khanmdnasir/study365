from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class TestSetAdmin(admin.TabularInline):
    model=TestSet

class TestQuestionAdmin(admin.TabularInline):
    model=TestQuestion

@admin.register(MockTest)
class MockTestAdmin(SummernoteModelAdmin):
    list_display=['id','title','category']
    inlines=[TestSetAdmin,TestQuestionAdmin]
    summernote_fields=('description',)

admin.site.register(MockTestRating)
admin.site.register(TestWishList)
admin.site.register(TestCart)
admin.site.register(UserTest)
admin.site.register(MyTestSet)
admin.site.register(MyMockTest)



