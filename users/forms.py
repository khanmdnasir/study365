from django import forms
from django.contrib.auth import password_validation
from django.db.models import fields

from .models import Student, User,Level_Choices,Department_Choices
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.forms import widgets
from django.forms.widgets import PasswordInput, TextInput
from django.utils.translation import gettext,gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class RegistrationForm(UserCreationForm):

    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'Last Name'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'Password'}))
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'Confirm Password'}))
    email=forms.CharField(required=True,label='Email',widget=forms.EmailInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'Email Address'}))
    phone_number=PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='BD',attrs={'class':'ps-4 mb-3 me-3','placeholder':'Phone Number'}))
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2','phone_number']
        widgets={'username':forms.TextInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'Username'})}

class IRegistrationForm(UserCreationForm):

    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'Last Name'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'Password'}))
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'Confirm Password'}))
    email=forms.CharField(required=True,label='Email',widget=forms.EmailInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'Email Address'}))
    phone_number=PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='BD',attrs={'class':'ps-4 mb-3 me-3','placeholder':'Phone Number'}))
    profile_image=forms.ImageField(widget=forms.FileInput(attrs={'class':'file-upload-input','onchange':'readURL(this);','accept':'image/*'}))
    nid_image=forms.ImageField(widget=forms.FileInput(attrs={'class':'file-upload-input2','onchange':'read2(this);','accept':'image/*'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2','phone_number','profile_image','nid_image']
        widgets={'username':forms.TextInput(attrs={'class':'ps-4 mb-3 me-3','placeholder':'Username'})}

class IRegistrationForm1(forms.ModelForm):
    phone_number=PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='BD',attrs={'class':'ps-4 mb-3 me-3','placeholder':'Phone Number'}))
    profile_image=forms.ImageField(widget=forms.FileInput(attrs={'class':'file-upload-input','onchange':'readURL(this);','accept':'image/*'}))
    nid_image=forms.ImageField(widget=forms.FileInput(attrs={'class':'file-upload-input2','onchange':'read2(this);','accept':'image/*'}))
    class Meta:
        model=User
        fields=['phone_number','profile_image','nid_image']

class IRegistrationForm2(forms.ModelForm):
    phone_number=PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='BD',attrs={'class':'ps-4 mb-3 me-3','placeholder':'Phone Number'}))
    nid_image=forms.ImageField(widget=forms.FileInput(attrs={'class':'file-upload-input2','onchange':'read2(this);','accept':'image/*'}))
    class Meta:
        model=User
        fields=['phone_number','profile_image','nid_image']
        


class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label=_("Confirm Password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter Your Email Address','class':'ps-4 mb-3'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','placeholder':'New Password','class':'ps-4 mb-2'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','placeholder':'Confirm Password','class':'ps-4 mb-4'}),
    )



class ProfileForm(forms.ModelForm):
    education_level=forms.ChoiceField(choices=Level_Choices,widget=forms.Select(attrs={'class':'form-select'}),required=False)
    department=forms.ChoiceField(choices=Department_Choices,widget=forms.Select(attrs={'class':'form-select'}),required=False)
    about=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'7','value':''}),required=False)
    class Meta:
        model=Student
        fields=['education_level','department','about']

class UserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)  
    address=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'6'}),required=False)
    profile_image=forms.ImageField(widget=forms.FileInput(attrs={'class':'file-upload-input','onchange':'readURL(this);','accept':'image/*'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','address','profile_image')

class EForm(forms.ModelForm):
    
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('email',)

class PForm(forms.ModelForm):
    
    phone_number=PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='BD',attrs={'class':'form-control mb-2'}))    
   
    class Meta:
        model = User
        fields = ('phone_number',)