from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.contrib import messages
from app.models import Instructor
from .forms import   EForm, PForm, ProfileForm, RegistrationForm, UserForm, VerifyForm
from .utils import account_activation_token
from .models import User,Student
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text
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
        uid = force_text(urlsafe_base64_decode(uidb64))
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
    if request.method=='GET':
        form=VerifyForm()
    else:
        form=VerifyForm(request.POST)
        if form.is_valid():
            verification_code = request.POST['code'] 
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
    return render(request, 'app/verification.html', {'form':form})

def verify_view1(request):
    if request.method=='GET':
        form=VerifyForm()
    else:
        form=VerifyForm(request.POST)
        if form.is_valid():
            verification_code = request.POST['code'] 
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
    return render(request, 'app/verification.html', {'form':form})


            


@login_required(redirect_field_name='home')
def stdprofile_view(request):
    
    
    
    p_active='active'
    return render(request,'app/studentProfile.html',{'p_active':p_active})

@login_required(redirect_field_name='home')
def edit_profile(request):
    
    pForm=ProfileForm(request.POST or None,instance=request.user.student)
    uForm=UserForm(request.POST or None,request.FILES or None,instance=request.user)
    if pForm.is_valid() and uForm.is_valid():
        
        
        uForm.save()
        pForm.save()
        messages.success(request,'Profile Updated Successfully')
    
    
    # student=Student.objects.filter(user=request.user)
    p_active='active'
    return render(request,'app/edit_profile.html',{'pForm':pForm,'uForm':uForm,'p_active':p_active})

@login_required(redirect_field_name='home')
def change_phone(request):
    uForm=PForm(request.POST or None,request.FILES or None,instance=request.user)
    if uForm.is_valid():
        uForm.save()
        request.user.is_phone_verified=False
        messages.success(request,'Contact Updated Successfully')
   
    as_active='active'
    return render(request,'app/change_phone.html',{'uForm':uForm,'as_active':as_active})

@login_required(redirect_field_name='home')
def change_email(request):
    
    uForm=EForm(request.POST or None,request.FILES or None,instance=request.user)
    if uForm.is_valid():
        uForm.save()
        request.user.is_email_verified=False
        messages.success(request,'Email Updated Successfully')

    as_active='active'
    return render(request,'app/change_email.html',{'uForm':uForm,'as_active':as_active})



@login_required(redirect_field_name='home')
def account_settings(request):
    
    
    as_active='active'
    return render(request,'app/account_settings.html',{'as_active':as_active})

