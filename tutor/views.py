from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render
from app.models import Category
from .forms import CourseForm
from app.models import *
from .models import Instructor
from users.models import Student, User
from users.forms import EForm, IRegistrationForm, IRegistrationForm1, IRegistrationForm2, PForm, RegistrationForm, UserForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from users.utils import account_activation_token
from twilio.rest import Client
import math, random
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.paginator import Paginator


account_sid = 'AC6ca36161db8b890f8763d35c7c8b3532'
auth_token = 'a85a433f78ca4d06ee2ecd2d12c34717'
client = Client(account_sid, auth_token)

@login_required(redirect_field_name='login')
def tutor_dashboard(request):
    active="active"
    insId=Instructor.objects.get(user=request.user)
    this_month = datetime.now().month
    total_course=len(Course.objects.filter(instructor_id=insId))
    course=Course.objects.filter(instructor_id=insId,course_year__month=this_month)
    users=User.objects.all()
    return render(request,'tutor/tutor_dashboard.html',{'users':users,'active1':active,'total_course':total_course,'course':course})

def tutor_signin(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('tutor:tutor_dashboard')
        else:
            return redirect('tutor:tutor_signup')
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
                    if user.is_teacher:
                        login(request,user)
                        return redirect('tutor:tutor_dashboard')  
                    else:
                        # messages.error(request, 'You are not registered as a tutor, Please signup as a tutor first.')
                        return redirect('tutor:tutor_signin')             
        
        return render(request,'tutor/tutor_signin.html',{'form':form})
    

def tutor_signup(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('tutor:tutor_dashboard')
        else:
            
            form=IRegistrationForm(instance=request.user)
           
            if request.method == 'POST':
                if request.user.profile_image:
                    form=IRegistrationForm1(request.POST or None,request.FILES or None,instance=request.user)
                else:
                    form=IRegistrationForm2(request.POST or None,request.FILES or None,instance=request.user)
               
                
                if form.is_valid() :
                    speciality=request.POST.getlist('speciality')
                    
                    user = form.save() 
                    Student.objects.create(user=user)
                    request.session['pk']=user.pk 
                    Instructor.objects.create(user=user,speciality=speciality)
                    
                    
                    otp=generateOTP()
                    # print(otp)
                    user.otp=otp
                    user.save()
                    # phone_number=""+str(user.phone_number)
                    
                
                    # client.messages.create(
                    #     to=phone_number, 
                    #     from_="+12058289469",
                    #     body="Hello from Python! ...your otp is "+otp)

                    
                    return redirect('verify1')
                    
            return render(request,'tutor/tutor_signup.html',{'form':form})
    else:
        
        form=IRegistrationForm()
        
        if request.method == 'POST':
            form=IRegistrationForm(request.POST or None,request.FILES or None)
            
            if form.is_valid() :
                
                user = form.save()
                Student.objects.create(user=user)
                request.session['pk']=user.pk 
                speciality=request.POST.getlist('speciality')
                Instructor.objects.create(user=user,speciality=speciality)
                otp=generateOTP()
                # print(otp)
                user.otp=otp
                user.save()
                # phone_number=""+str(user.phone_number)
                
                
                
                # current_site = get_current_site(request)
                # mail_subject = 'Activate your account.'
                # message = render_to_string('app/activate.html', {
                #             'user': user,
                #             'domain': current_site.domain,
                #             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                #             'token': account_activation_token.make_token(user),
                #         })
                # to_email = form.cleaned_data.get('email')
                # send_mail(mail_subject, message, 'nasirkhan97.bd@gmail.com', [to_email])
                # client.messages.create(
                #     to=phone_number, 
                #     from_="+12058289469",
                #     body="Hello from Python! ...your otp is "+otp)

                
                return redirect('verify')
                
                
        return render(request,'tutor/tutor_signup.html',{'form':form})
   
def generateOTP():
  digits = "0123456789"
  OTP = ""
#   print("OTP Generation")
  for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
  return OTP

@login_required(redirect_field_name='login')
def tutor_profile(request):
    tutor=Instructor.objects.get(user=request.user)
    uForm=UserForm(instance=request.user)
   
    if request.method == 'POST':
        uForm=UserForm(request.POST or None,request.FILES or None,instance=request.user)
        if uForm.is_valid():
            uForm.save()
            overview=request.POST.get('overview')
            speciality=request.POST.getlist('speciality')
            Instructor.objects.filter(user=request.user).update(instructor_intro=overview,speciality=speciality)
            tutor=Instructor.objects.get(user=request.user)
            return redirect('tutor:tutor_profile')
    return render(request,'tutor/edit_tprofile.html',{'tutor':tutor,'uForm':uForm})
    

@login_required(redirect_field_name='login')
def addCourse(request):
    active="active"
    category=Category.objects.all()
    users=User.objects.all()
    if request.method == 'POST':
        cimage=request.FILES.get('course_image')
        ctitle=request.POST.get('course_title')
        cid=request.POST.get('category')
        price=request.POST.get('price')
        offer=request.POST.get('offer')
        duration=request.POST.get('duration')
        language=request.POST.get('language')
        overview=request.POST.get('overview')
        includes=request.POST.get('includes')
        include_arr=includes.split(',')
        description=request.POST.get('description')
        outcome=request.POST.get('outcome')
        outcome_arr=outcome.split(',')
        target=request.POST.get('target')
        target_arr=target.split(',')
        course=Course.objects.create(instructor_id=Instructor.objects.get(user=request.user),course_image=cimage,course_title=ctitle,course_category=Category.objects.get(id=cid),course_overview=overview,course_language=language,course_price=price,course_offer=offer,course_include=include_arr,course_outcome=outcome_arr,course_description=description,course_target=target_arr,course_duration=duration)
        
        return redirect('tutor:addChapter',id=course.id)
    return render(request,'tutor/addCourse.html',{'users':users,'active3':active,'category':category})

@login_required(redirect_field_name='login')
def editCourse(request,id):
    active='active'
    course=Course.objects.get(id=id)
    users=User.objects.all()
    category=Category.objects.all()
    if request.method == 'POST':
        cimage=request.FILES.get('course_image')
        ctitle=request.POST.get('course_title')
        cid=request.POST.get('category')
        price=request.POST.get('price')
        offer=request.POST.get('offer')
        duration=request.POST.get('duration')
        language=request.POST.get('language')
        overview=request.POST.get('overview')
        includes=request.POST.get('includes')
        include_arr=includes.split(',')
        description=request.POST.get('description')
        outcome=request.POST.get('outcome')
        outcome_arr=outcome.split(',')
        target=request.POST.get('target')
        target_arr=target.split(',')
        messages.success(request, 'Course updated Successfully.')
        if cimage:
            Course.objects.filter(id=id).update(course_image=cimage,course_title=ctitle,course_category=Category.objects.get(id=cid),course_overview=overview,course_language=language,course_price=price,course_offer=offer,course_include=include_arr,course_outcome=outcome_arr,course_description=description,course_target=target_arr,course_duration=duration)
        else:
            Course.objects.filter(id=id).update(course_title=ctitle,course_category=Category.objects.get(id=cid),course_overview=overview,course_language=language,course_price=price,course_offer=offer,course_include=include_arr,course_outcome=outcome_arr,course_description=description,course_target=target_arr,course_duration=duration)
        return redirect('tutor:singleCourse',id=id)   
    return render(request,'tutor/addCourse.html',{'users':users,'active3':active,'category':category,'course':course})

@login_required(redirect_field_name='login')
def deleteCourse(request,id):
    Course.objects.get(id=id).delete()
    return redirect('tutor:myCourse')

@login_required(redirect_field_name='login')
def coursePublish(request,id):
    course=Course.objects.get(id=id)
    course.is_publish=True
    course.save()
    return redirect('tutor:singleCourse',id=id)

@login_required(redirect_field_name='login')
def addChapter(request,id):
    active="active"  
    course=Course.objects.get(pk=id)
    chapters=Chapter.objects.filter(course_id=course).order_by('chapter_position')
    lessons=Lesson.objects.filter(course_id=course).order_by('lesson_position')
    users=User.objects.all()
    if request.method == 'POST':
        chapter_name=request.POST.get('chapter_title')
        chapter_position=request.POST.get('chapter_position')
        chapter=Chapter.objects.update_or_create(course_id=course,chapter_name=chapter_name,chapter_position=chapter_position)
        messages.success(request, 'Chapter added Successfully.')
    return render(request,'tutor/addChapter.html',{'users':users,'active4':active,'course':course,'chapters':chapters,'lessons':lessons})

@login_required(redirect_field_name='login')
def editChapter(request,id):
    active="active"   
    chapter=Chapter.objects.get(pk=id)
    cid=Course.objects.get(id=chapter.course_id.id)
    chapters=Chapter.objects.filter(course_id=cid).order_by('chapter_position')
    lessons=Lesson.objects.filter(course_id=cid).order_by('lesson_position')
    users=User.objects.all()
    if request.method == 'POST':
        chapter_name=request.POST.get('chapter_title')
        chapter_position=request.POST.get('chapter_position')
        Chapter.objects.filter(pk=id).update(chapter_name=chapter_name,chapter_position=chapter_position)
        chapter=Chapter.objects.get(pk=id)
        messages.success(request, 'Chapter updated Successfully.')
    return render(request,'tutor/addChapter.html',{'users':users,'active4':active,'course':cid,'chapters':chapters,'lessons':lessons,'chapter':chapter})

@login_required(redirect_field_name='login')
def deleteChapter(request,id):
    chapter=Chapter.objects.get(id=id)    
    chapter.delete()
    messages.success(request, 'Chapter deleted Successfully.')
    return redirect('tutor:addChapter',id=chapter.course_id.id)

@login_required(redirect_field_name='login')
def addLesson(request,id1,id2):
    active="active"   
    course=Course.objects.get(pk=id1)
    chapter=Chapter.objects.get(pk=id2)
    chapters=Chapter.objects.filter(course_id=course).order_by('chapter_position')
    lessons=Lesson.objects.filter(course_id=course).order_by('lesson_position')
    users=User.objects.all()
    if request.method == 'POST':
        lesson_type=request.POST.get('lesson_type')
        lesson_position=request.POST.get('lesson_position') 
        lesson_title=request.POST.get('lesson_title')
        if (lesson_type == 'V'):            
            tf=TempFile.objects.filter(user=request.user)[:1].get()
            if tf:                 
                Lesson.objects.create(course_id=course,chapter_id=chapter,lesson_title=lesson_title,lesson_type=lesson_type,lesson_video=tf.file,lesson_position=lesson_position)
                tf.delete()
        if (lesson_type == 'I'):            
            instruction=request.POST.get('instruction')                   
            Lesson.objects.create(course_id=course,chapter_id=chapter,lesson_title=lesson_title,lesson_type=lesson_type,lesson_position=lesson_position,text_instruction=instruction)
        if (lesson_type == 'A'):            
            ainstruction=request.POST.get('ainstruction')                  
            total_mark=request.POST.get('total_mark')                  
            pass_mark=request.POST.get('pass_mark') 
            afile=request.FILES.get('asfile')                 
            Lesson.objects.create(course_id=course,chapter_id=chapter,lesson_title=lesson_title,lesson_type=lesson_type,assignment_total_mark=total_mark,assignment_pass_mark=pass_mark,assignment_instruction=ainstruction,assignment_file=afile,lesson_position=lesson_position)
        if (lesson_type == 'Q'):            
            quiz_instruction=request.POST.get('quiz_instruction')                 
            quiz_time=request.POST.get('quiz_time')                 
            quiz_total_mark=request.POST.get('quiz_total_mark')                 
            quiz_pass_mark=request.POST.get('quiz_pass_mark')                 
            lesson=Lesson.objects.create(course_id=course,chapter_id=chapter,lesson_title=lesson_title,lesson_type=lesson_type,lesson_position=lesson_position,quiz_instruction=quiz_instruction,quiz_time=quiz_time,quiz_total_mark=quiz_total_mark,quiz_pass_mark=quiz_pass_mark)
            return redirect('tutor:addQuiz',id=lesson.id)
        messages.success(request, 'Lesson added Successfully.')
    return render(request,'tutor/addLesson.html',{'users':users,'active4':active,'course':course,'chapters':chapters,'lessons':lessons})

@login_required(redirect_field_name='login')
def editLesson(request,id):
    active="active" 
    lesson=Lesson.objects.get(pk=id)
    course=Course.objects.get(pk=lesson.course_id.id)
    chapter=Chapter.objects.get(pk=lesson.chapter_id.id)
    chapters=Chapter.objects.filter(course_id=course).order_by('chapter_position')
    lessons=Lesson.objects.filter(course_id=course).order_by('lesson_position')
    users=User.objects.all()
    if request.method == 'POST':
        lesson_type=request.POST.get('lesson_type')
        lesson_position=request.POST.get('lesson_position') 
        lesson_title=request.POST.get('lesson_title')
        if (lesson_type == 'V'):            
            
            tf=TempFile.objects.filter(user=request.user)[:1].get()
            
            if tf:            
                Lesson.objects.filter(pk=id).update(lesson_title=lesson_title,lesson_type=lesson_type,lesson_video=tf.file,lesson_position=lesson_position)
                tf.delete()
            
        if (lesson_type == 'I'):            
            instruction=request.POST.get('instruction')                   
            Lesson.objects.filter(pk=id).update(lesson_title=lesson_title,lesson_type=lesson_type,lesson_position=lesson_position,text_instruction=instruction)
        if (lesson_type == 'A'):            
            ainstruction=request.POST.get('ainstruction')               
            total_mark=request.POST.get('total_mark')                  
            pass_mark=request.POST.get('pass_mark') 
            afile=request.FILES.get('asfile')   
            
            if afile is not None:              
                Lesson.objects.filter(pk=id).update(lesson_title=lesson_title,lesson_type=lesson_type,assignment_total_mark=total_mark,assignment_pass_mark=pass_mark,assignment_instruction=ainstruction,assignment_file=afile,lesson_position=lesson_position)
            else:
                Lesson.objects.filter(pk=id).update(lesson_title=lesson_title,lesson_type=lesson_type,assignment_total_mark=total_mark,assignment_pass_mark=pass_mark,assignment_instruction=ainstruction,lesson_position=lesson_position)

        if (lesson_type == 'Q'):            
            quiz_instruction=request.POST.get('quiz_instruction')                 
            quiz_time=request.POST.get('quiz_time')                 
            quiz_total_mark=request.POST.get('quiz_total_mark')                 
            quiz_pass_mark=request.POST.get('quiz_pass_mark')                 
            Lesson.objects.filter(pk=id).update(lesson_title=lesson_title,lesson_type=lesson_type,lesson_position=lesson_position,quiz_instruction=quiz_instruction,quiz_time=quiz_time,quiz_total_mark=quiz_total_mark,quiz_pass_mark=quiz_pass_mark)
        messages.success(request, 'Lesson updated Successfully.')
    return render(request,'tutor/addLesson.html',{'users':users,'active4':active,'course':course,'chapters':chapters,'lessons':lessons,'lesson':lesson})   
    

@login_required(redirect_field_name='login')
def deleteLesson(request,id):
    lesson=Lesson.objects.get(id=id)    
    lesson.delete()
    messages.success(request, 'Lesson deleted Successfully.')
    return redirect('tutor:addChapter',id=lesson.course_id.id)

@login_required(redirect_field_name='login')
def addQuiz(request,id):
    active='active'
    lesson=Lesson.objects.get(pk=id)
    quizes=Quiz.objects.filter(lesson=lesson)
    course=Course.objects.get(pk=lesson.course_id.id)
    chapters=Chapter.objects.filter(course_id=course).order_by('chapter_position')
    lessons=Lesson.objects.filter(course_id=course).order_by('lesson_position')
    users=User.objects.all()
    if request.method == 'POST':
        question=request.POST.get('question')
        qposition=request.POST.get('qposition')
        option1=request.POST.get('option1')
        option2=request.POST.get('option2')
        option3=request.POST.get('option3')
        option4=request.POST.get('option4')
        option=[]
        option.append(option1)
        option.append(option2)
        option.append(option3)
        option.append(option4)
        correct=request.POST.get('correct')
        Quiz.objects.create(course=course,lesson=lesson,question=question,quiz_position=qposition,option=option,correct_answer=correct)
        messages.success(request, 'Quiz added Successfully.')
    return render(request,'tutor/addQuiz.html',{'users':users,'active4':active,'course':course,'chapters':chapters,'lessons':lessons,'quizes':quizes})

@login_required(redirect_field_name='login')
def editQuiz(request,id):
    active='active'
    quiz=Quiz.objects.get(pk=id)
    lesson=Lesson.objects.get(pk=quiz.lesson.id)
    quizes=Quiz.objects.filter(lesson=lesson)
    course=Course.objects.get(pk=lesson.course_id.id)
    chapters=Chapter.objects.filter(course_id=course).order_by('chapter_position')
    lessons=Lesson.objects.filter(course_id=course).order_by('lesson_position')
    users=User.objects.all()
    if request.method == 'POST':
        question=request.POST.get('question')
        qposition=request.POST.get('qposition')
        option1=request.POST.get('option1')
        option2=request.POST.get('option2')
        option3=request.POST.get('option3')
        option4=request.POST.get('option4')
        option=[]
        option.append(option1)
        option.append(option2)
        option.append(option3)
        option.append(option4)
        correct=request.POST.get('correct')
        
        Quiz.objects.filter(pk=id).update(question=question,quiz_position=qposition,option=option,correct_answer=correct)
        messages.success(request, 'Quiz updated Successfully.')
        return render(request,'tutor/addQuiz.html',{'active4':active,'course':course,'chapters':chapters,'lessons':lessons,'quizes':quizes})
    return render(request,'tutor/addQuiz.html',{'users':users,'active4':active,'course':course,'chapters':chapters,'lessons':lessons,'quiz':quiz})

@login_required(redirect_field_name='login')
def deleteQuiz(request,id):
    quiz=Quiz.objects.get(id=id)
    quiz.delete()
    messages.success(request, 'Quiz deleted Successfully.')
    return redirect('tutor:addQuiz',id=quiz.lesson.id)

@login_required(redirect_field_name='login')
def myCourse(request):
    active="active"
    this_month = datetime.now().month
    insId=Instructor.objects.get(user=request.user)
    course=Course.objects.filter(instructor_id=insId,course_year__month=this_month)
    mycourse=Course.objects.filter(instructor_id=insId)
    mycategory=mycourse.distinct('course_category')
    users=User.objects.all()
    return render(request,'tutor/myCourse.html',{'users':users,'active4':active,'course':course,'mycategory':mycategory,'mycourse':mycourse})

@login_required(redirect_field_name='login')
def singleCourse(request,id):
    active="active"
    course=Course.objects.get(pk=id)   
    range1=math.ceil(len(course.course_outcome)/2)
    chapters=Chapter.objects.filter(course_id=id).order_by("chapter_position")    
    lessons=Lesson.objects.filter(course_id=id).order_by("lesson_position")
    users=User.objects.all()
    return render(request,'tutor/singleCourse.html',{'users':users,'active4':active,'course':course,'range1':range1,'chapters':chapters,'lessons':lessons})



@login_required(redirect_field_name='login')
def myStudents(request):
    active="active"
    myStudents=MyCourse.objects.filter(instructor=Instructor.objects.get(user=request.user))
    search=request.GET.get('search')
    ppage=str(request.GET.get('perpage'))
    page_number=request.GET.get('page')
    if search != '' and search is not None:
        myStudents.filter(course=Course.objects.filter(course_title__icontains=search))
    
    if ppage != 'None' and ppage != '':
        paginator=Paginator(myStudents,ppage)
    else:
        paginator=Paginator(myStudents,15)
    
    page_obj=paginator.get_page(page_number)
    users=User.objects.all()
    return render(request,'tutor/myStudents.html',{'users':users,'active5':active,'page_obj':page_obj})

@login_required(redirect_field_name='login')
def allSubmission(request):
    active="active"
    courses=Course.objects.filter(instructor_id=Instructor.objects.get(user=request.user))
    submissions=StudentAssignment.objects.filter(instructor=Instructor.objects.get(user=request.user))
    search=request.GET.get('search')
    date=request.GET.get('date')
    course=request.GET.get('course')
    ppage=str(request.GET.get('perpage'))
    page_number=request.GET.get('page')
    if search != '' and search is not None:
        submissions.filter(user=User.objects.filter(first_name__icontains=search))

    if date != '' and date is not None:
        submissions.filter(submitted_date__contains=date)

    if course != '' and course is not None:
        submissions.filter(course__contains=course)
    
    if ppage != 'None' and ppage != '':
        paginator=Paginator(submissions,ppage)
    else:
        paginator=Paginator(submissions,15)
    
    page_obj=paginator.get_page(page_number)
    if request.method == "POST":
        sid=request.POST.get('sid')
        mark=request.POST.get('obtain_mark')
        sa=StudentAssignment.objects.get(id=sid)
        if int(mark) < sa.lesson.assignment_total_mark:
            sa.mark=mark
            sa.save()
            messages.success(request,'Mark Updated Successfully')
        else:
            messages.error(request,'Invalid Mark, mark can not be getter than total mark')
    users=User.objects.all()
    return render(request,'tutor/allSubmission.html',{'users':users,'active6':active,'page_obj':page_obj,'courses':courses})

@login_required(redirect_field_name='login')
def guidelines(request):
    active="active"
    return render(request,'tutor/guidelines.html',{'active7':active})

@login_required(redirect_field_name='login')
def payment(request):
    active="active"
    return render(request,'tutor/payment.html',{'active9':active})

@login_required(redirect_field_name='login')
def helpSupport(request):
    active="active"
    return render(request,'tutor/help&support.html',{'active8':active})

@login_required(redirect_field_name='login')
def settings(request):
    active="active"
    return render(request,'tutor/settings.html',{'active10':active})