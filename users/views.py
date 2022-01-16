from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.contrib import messages
from app.models import Category, Instructor
from .forms import   EForm, PForm, ProfileForm, RegistrationForm, UserForm
from .utils import account_activation_token
from .models import User,Student
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
import json
from twilio.rest import Client
import math, random
from django.contrib.auth.decorators import login_required
from django.conf import settings


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=AuthenticationForm()
        form.fields['username'].widget.attrs['placeholder']='Enter Username or Email Address'
        form.fields['username'].widget.attrs['class']='ps-4 mb-3'
        form.fields['password'].widget.attrs['placeholder']='Enter Your Password'
        form.fields['password'].widget.attrs['class']='ps-4 mb-3'
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            form.fields['username'].widget.attrs['placeholder']='Enter Username or Email Address'
            form.fields['username'].widget.attrs['class']='ps-4 mb-3'
            form.fields['password'].widget.attrs['placeholder']='Enter Your Password'
            form.fields['password'].widget.attrs['class']='ps-4 mb-3'
            if form.is_valid():
                uname=form.cleaned_data['username']
                password=form.cleaned_data['password']
                
                user=authenticate(request,username=uname,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')                                 
            
        return render(request, 'app/login.html',{'form':form})
        

def registration_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='GET':
            form=RegistrationForm()
        else:
            form=RegistrationForm(request.POST)
            if form.is_valid():
                
                user = form.save() 
                request.session['pk']=user.pk 
                Student.objects.create(user=user)
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('app/activate.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': account_activation_token.make_token(user),
                        })
                to_email = form.cleaned_data.get('email')
                send_mail(mail_subject, message, 'nasirkhan97.bd@gmail.com', [to_email])
                
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                return render(request,'app/verification_success.html')
        return render(request,'app/registration.html',{'form':form})





def activate_user(request, uidb64, token):
    
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_email_verified=True
        user.save()
        return render(request,'app/activation_success.html')
    else:
        return HttpResponse('Activation link is invalid!')



def verify_view(request):
    if request.method == 'POST':
        otp1=request.POST.get('otp1')
        otp2=request.POST.get('otp2')
        otp3=request.POST.get('otp3')
        otp4=request.POST.get('otp4')
        

        verification_code = ''+otp1+otp2+otp3+otp4
        pk=request.session.get('pk') 
        user=User.objects.get(pk=pk) 
                
        if verification_code==user.otp:
        #    new_user=authenticate(request,username=user.username,password=user.password) 
            login(request,user,backend='django.contrib.auth.backends.ModelBackend') 
            
            user.is_teacher=True               
            user.is_phone_verified = True
            user.save()
            
            return render(request,'tutor/tutor_signup_success.html')
        else:
            messages.add_message(request, messages.ERROR,
                            'Verification Failled')
    return render(request, 'app/verification.html')

def verify_view1(request):
    if request.method == 'POST':
        otp1=request.POST.get('otp1')
        otp2=request.POST.get('otp2')
        otp3=request.POST.get('otp3')
        otp4=request.POST.get('otp4')
        

        verification_code = ''+otp1+otp2+otp3+otp4
        pk=request.session.get('pk') 
        user=User.objects.get(pk=pk) 
                
        if verification_code==user.otp:
        #    new_user=authenticate(request,username=user.username,password=user.password) 
            
            
            user.is_teacher=True               
            user.is_phone_verified = True
            user.save()
            
            return render(request,'tutor/tutor_signup_success.html')
        else:
            messages.add_message(request, messages.ERROR,
                            'Verification Failled')
    return render(request, 'app/verification.html')


            


@login_required(redirect_field_name='home')
def stdprofile_view(request):
    categories=Category.objects.all()
    p_active='active'
    users=User.objects.all()
    return render(request,'app/studentProfile.html',{'p_active':p_active,'categories':categories,'users':users})

@login_required(redirect_field_name='home')
def edit_profile(request):
    
    try:
        pForm=ProfileForm(request.POST or None,instance=request.user.student)
    except:
        Student.objects.create(user=request.user)
        pForm=ProfileForm(request.POST or None,instance=request.user.student)
    uForm=UserForm(request.POST or None,request.FILES or None,instance=request.user)
    categories=Category.objects.all()
    p_active='active'
    users=User.objects.all()
    if pForm.is_valid() and uForm.is_valid():
        
        
        uForm.save()
        pForm.save()
        
        return render(request,'app/studentProfile.html',{'users':users,'pForm':pForm,'uForm':uForm,'p_active':p_active,'categories':categories})
    
    # student=Student.objects.filter(user=request.user)
    
    return render(request,'app/edit_profile.html',{'users':users,'pForm':pForm,'uForm':uForm,'p_active':p_active,'categories':categories})

@login_required(redirect_field_name='home')
def change_phone(request):
    uForm=PForm(request.POST or None,request.FILES or None,instance=request.user)
    categories=Category.objects.all()
    as_active='active'
    users=User.objects.all()
    if uForm.is_valid():
        uForm.save()
        request.user.is_phone_verified=False
        messages.success(request,'Contact Updated Successfully')
       
    return render(request,'app/change_phone.html',{'uForm':uForm,'as_active':as_active,'categories':categories,'users':users})

@login_required(redirect_field_name='home')
def change_email(request):
    categories=Category.objects.all()
    as_active='active'
    users=User.objects.all()
    uForm=EForm(request.POST or None,request.FILES or None,instance=request.user)
    if uForm.is_valid():
        uForm.save()
        request.user.is_email_verified=False
        messages.success(request,'Email Updated Successfully')

    return render(request,'app/change_email.html',{'uForm':uForm,'as_active':as_active,'categories':categories,'users':users})



# @login_required(redirect_field_name='home')
# def account_settings(request):
    
    
#     as_active='active'
#     return render(request,'app/account_settings.html',{'as_active':as_active})

