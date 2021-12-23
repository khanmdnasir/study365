from django import forms

from app.models import Category, Course
from tutor.models import Instructor

Language_Choice=(
    ('english','English'),
    ('bangla','Bangla')
)


class CourseForm(forms.ModelForm):
    course_category=forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-select  mb-3 color-grey'}))
    course_title=forms.CharField(widget=forms.TextInput(attrs={'class':'px-3 tchAddCourseTopRightinput bg-white','placeholder':'type Course Title'}))
    course_image=forms.ImageField(widget=forms.FileInput(attrs={'class':'file-upload-input','onchange':'readURL(this);'}))
    course_overview=forms.CharField(widget=forms.Textarea(attrs={'class':'p-2 w-100','rows':'7','placeholder':'Type Here'}))
    course_language=forms.ChoiceField(choices=Language_Choice,widget=forms.Select(attrs={'form-select mb-3 color-grey'}))
    course_price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'px-2 tchAddCourseTopRightinput bg-white','placeholder':'Type Here Price....'}))
    course_offer=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'mx-2 bg-white px-2'}))
    course_include=forms.TypedMultipleChoiceField(widget=forms.SelectMultiple(attrs={}))
    course_outcome=forms.TypedMultipleChoiceField(widget=forms.SelectMultiple(attrs={}))
    course_description=forms.CharField(widget=forms.Textarea(attrs={'class':'p-2 w-100','rows':'7','placeholder':'Type Here'}))
    course_target=forms.TypedMultipleChoiceField(widget=forms.SelectMultiple(attrs={}))    
    course_duration=forms.DurationField(widget=forms.TextInput(attrs={'class':'color-grey fw-bold mb-1'}))

    class Meta:
        model=Course
        fields=['course_category','course_title','course_image','course_overview','course_language','course_price','course_offer','course_include','course_outcome','course_description','course_target','course_duration']

