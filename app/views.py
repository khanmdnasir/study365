from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core import paginator
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect

from mocktest.models import MockTest, TestCart, TestWishList,MyMockTest

from .serializers import LessonSerializer
from .models import *
import math
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator




# Create your views here.
def home(request):
    pcategories=Category.objects.filter(is_popular=True)
    fcategories=Category.objects.filter(is_featured=True)
    categories=Category.objects.all()
    courses=Course.objects.filter(is_active=True,is_publish=True)
    fcourses=courses.filter(is_featured=True)
    total_course=courses.count
    books=Book.objects.all()
    total_book=books.count
    # pcourses=Course.objects.filter(is_popular=True).order_by('id').exclude(id__in=CourseWishList.objects.filter(user=request.user).values_list('course'))
    pcourses=courses.filter(is_popular=True)
    fbooks=Book.objects.filter(book_featured=True)
    bwishlist=[]
    cwishlist=[]
    if request.user.is_authenticated:
        bw=BookWishList.objects.filter(user=request.user)
        for b in bw:
            bwishlist.append(b.book)
        cw=CourseWishList.objects.filter(user=request.user)
        for c in cw:
            cwishlist.append(c.course)

    users=User.objects.all()  
    
    return render(request,'app/home.html',{'users':users,'fcourses':fcourses,'bwishlist':bwishlist,'cwishlist':cwishlist,'pcategories':pcategories,'fcategories':fcategories,'pcourses':pcourses,'categories':categories,'fbooks':fbooks,'total_course':total_course,'total_book':total_book})

def find_course(request,pk=None):
    
    search_query=request.GET.get('search')
    checkboxs=request.GET.getlist('checkbox')
    try:
        rate=int(request.GET.get('flexRadioDefault'))
    except:
        rate=''
    minPrice=request.GET.get('minPrice')
    maxPrice=request.GET.get('maxPrice')
    ppage=str(request.GET.get('perpage'))
    page_number=request.GET.get('page')
    categories=Category.objects.all()
        
    cwishlist=[]
    if request.user.is_authenticated:
        
        cw=CourseWishList.objects.filter(user=request.user)
        for c in cw:
            cwishlist.append(c.course)
    users=User.objects.all() 
    courses=Course.objects.filter(is_active=True,is_publish=True).order_by('id')
    if courses:
        minp=courses.order_by('course_price').first()
        maxp=courses.order_by('course_price').last()
        if pk is not None:
            courses=courses.filter(course_category=pk)

        if search_query != '' and search_query is not None:
            courses=courses.filter(course_title__icontains=search_query)
        
        if checkboxs:
            courses=courses.filter(course_category__in=checkboxs)
            
        if rate != 'None' and rate != '':
            filter_id = [x.id for x in Course.objects.all() if x.course_rating == rate]
            courses=courses.filter(id__in=filter_id)
        
        if minPrice != '' and maxPrice != '' and minPrice is not None and maxPrice is not None:
            courses=courses.filter(course_price__range=[minPrice,maxPrice])
        else:
            minPrice=minp.course_price
            maxPrice=maxp.course_price
            
        if ppage != 'None' and ppage != '':
            paginator=Paginator(courses,ppage)
        else:
            
            paginator=Paginator(courses,15)
        
        page_obj=paginator.get_page(page_number)
      
        return render(request,'app/FindCourses.html',{'users':users,'page_obj':page_obj,'categories':categories,'minPrice':minPrice,'maxPrice':maxPrice,'rate':rate,'cwishlist':cwishlist,'minp':minp,'maxp':maxp})
    else:
        return render(request,'app/FindCourses.html',{'users':users,'categories':categories,'cwishlist':cwishlist})

def course_details(request,pk):
    
    course=Course.objects.get(pk=pk)
    categories=Category.objects.all()
    
    range1=math.ceil(len(course.course_outcome)/2)
    chapters=Chapter.objects.filter(course_id=pk).order_by("chapter_position")
    
    lessons=Lesson.objects.filter(course_id=pk).order_by("lesson_position")
    rcourses=Course.objects.filter(course_category=course.course_category,is_active=True,is_publish=True)
    ratings=CourseRating.objects.filter(course=course)
    cwishlist=[]
    if request.user.is_authenticated:
        
        cw=CourseWishList.objects.filter(user=request.user)
        for c in cw:
            cwishlist.append(c.course)
    users=User.objects.all()
    return render(request,'app/singleCourse.html',{'users':users,'course':course,'range1':range1,'chapters':chapters,'lessons':lessons,'rcourses':rcourses,'categories':categories,'cwishlist':cwishlist,'ratings':ratings})



def all_books(request,pk=None):
    search_query=request.GET.get('search')
    checkboxs=request.GET.getlist('checkbox')
    minPrice=request.GET.get('minPrice')
    maxPrice=request.GET.get('maxPrice')
    ppage=str(request.GET.get('perpage'))
    page_number=request.GET.get('page')

    books=Book.objects.all().order_by('id')
    minp=books.order_by('book_price').first()
    maxp=books.order_by('book_price').last()
    if pk is not None:
        books=books.filter(course_category=pk)
    
    if search_query != '' and search_query is not None:
        books=books.filter(book_title__icontains=search_query)
    
    
    
    
    if checkboxs:
        books=books.filter(book_category__in=checkboxs)
    
    
    
    if minPrice != '' and maxPrice != '' and minPrice is not None and maxPrice is not None:
        books=books.filter(book_price__range=[minPrice,maxPrice])
    else:
        minPrice=minp.book_price
        maxPrice=maxp.book_price
    
    # print(ppage)
    if ppage != 'None' and ppage != '':
        paginator=Paginator(books,ppage)
    else:
        paginator=Paginator(books,15)
    
    page_obj=paginator.get_page(page_number)
    categories=Category.objects.all()
    bwishlist=[]
    if request.user.is_authenticated:
        bw=BookWishList.objects.filter(user=request.user)
        for b in bw:
            bwishlist.append(b.book)
    users=User.objects.all()    
    return render(request,'app/library.html',{'users':users,'page_obj':page_obj,'categories':categories,'minPrice':minPrice,'maxPrice':maxPrice,'bwishlist':bwishlist,'minp':minp,'maxp':maxp})

def book_details(request,pk):
    book=Book.objects.get(pk=pk)
    rbooks=Book.objects.filter(book_category=book.book_category)
    categories=Category.objects.all()
    ratings=BookRating.objects.filter(book=book)
    bwishlist=[]
    if request.user.is_authenticated:
        bw=BookWishList.objects.filter(user=request.user)
        for b in bw:
            bwishlist.append(b.book)
    users=User.objects.all()
    return render(request,'app/singleBook.html',{'users':users,'categories':categories,'book':book,'rbooks':rbooks,'bwishlist':bwishlist,'ratings':ratings})



@login_required(redirect_field_name='login')
def ccourses(request):
    mycourses=MyCourse.objects.filter(user=request.user)
    cc_active='active'
    categories=Category.objects.all()
    users=User.objects.all()
    return render(request,'app/continue_courses.html',{'users':users,'cc_active':cc_active,'categories':categories,'mycourses':mycourses})

@login_required(redirect_field_name='login')
def mybooks(request):
    mybooks=MyBooks.objects.filter(user=request.user)
    mb_active='active'
    categories=Category.objects.all()
    users=User.objects.all()
    return render(request,'app/mybooks.html',{'users':users,'mb_active':mb_active,'categories':categories,'mybooks':mybooks})

@login_required(redirect_field_name='login')
def wishlist(request):
    cwishlist=CourseWishList.objects.filter(user=request.user)
    bwishlist=BookWishList.objects.filter(user=request.user)
    mwishlist=TestWishList.objects.filter(user=request.user)
    categories=Category.objects.all()
    w_active='active'
    users=User.objects.all()
    return render(request,'app/wishlist.html',{'users':users,'w_active':w_active,'cwishlist':cwishlist,'bwishlist':bwishlist,'mwishlist':mwishlist,'categories':categories})

@login_required(redirect_field_name='login')
def payment_method(request):
    categories=Category.objects.all()
    pm_active='active'
    users=User.objects.all()
    return render(request,'app/payment_method.html',{'users':users,'pm_active':pm_active,'categories':categories})


@login_required(redirect_field_name='login')
def helpdesk(request):
    categories=Category.objects.all()
    hd_active='active'
    users=User.objects.all()
    return render(request,'app/helpdesk.html',{'users':users,'hd_active':hd_active,'categories':categories})

@login_required(redirect_field_name='login')
def addToCourseWishList(request):
    cid=request.GET['product']
    course=Course.objects.get(pk=cid)
    data={}
    checkw=CourseWishList.objects.filter(course=course,user=request.user).count()
    checkc=CourseCart.objects.filter(course=course,user=request.user).count()
    if checkc > 0:
        data={
            'string': 'Item already added to card'
        }
    else:
        if checkw > 0:
            wishlist=CourseWishList.objects.get(course=course,user=request.user)
            wishlist.delete()
            data={
                'string': 'Item delete from wishlist'
            }
        else:
            CourseWishList.objects.create(
                course=course,
                user=request.user
            )
            data={
                'string': 'Item added to wishlist'
            }
    return JsonResponse(data)

@login_required(redirect_field_name='login')
def DeleteCourseWishList(request):
    if request.method=='POST':
        course_id=request.POST.get('course_id')
        course=Course.objects.get(id=course_id)
        cw=CourseWishList.objects.get(course=course,user=request.user)
        cw.delete()
        
        return redirect('wishlist')

@login_required(redirect_field_name='login')
def DeleteTestWishList(request):
    if request.method=='POST':
        test_id=request.POST.get('m_id')
        test=MockTest.objects.get(id=test_id)
        tw=TestWishList.objects.get(test=test,user=request.user)
        tw.delete()
        
        return redirect('wishlist')


    



@login_required(redirect_field_name='login')
def addToBookWishList(request):
    cid=request.GET['product']
    book=Book.objects.get(pk=cid)
    data={}
    checkw=BookWishList.objects.filter(book=book,user=request.user).count()
    checkc=BookCart.objects.filter(book=book,user=request.user).count()
    if checkc > 0:
        data={
            'string': 'Item already added to card'
        }
    else:
        if checkw > 0:
            wishlist=BookWishList.objects.get(book=book,user=request.user)
            wishlist.delete()
            data={
                'string': 'Item delete from wishlist'
            }
        else:
            BookWishList.objects.create(
                book=book,
                user=request.user
            )
            data={
                'string': 'Item added to wishlist'
            }
    return JsonResponse(data)

@login_required(redirect_field_name='login')
def addToTestWishList(request):
    tid=request.GET['product']
    test=MockTest.objects.get(pk=tid)
    data={}
    checkw=TestWishList.objects.filter(test=test,user=request.user).count()
    checkc=TestCart.objects.filter(test=test,user=request.user).count()
    if checkc > 0:
        data={
            'string': 'Item already added to card'
        }
    else:
        if checkw > 0:
            wishlist=TestWishList.objects.get(test=test,user=request.user)
            wishlist.delete()
            data={
                'string': 'Item delete from wishlist'
            }
        else:
            TestWishList.objects.create(
                test=test,
                user=request.user
            )
            data={
                'string': 'Item added to wishlist'
            }
    return JsonResponse(data)

@login_required(redirect_field_name='login')
def DeleteBookWishList(request):
    if request.method=='POST':
        
        book_id=request.POST.get('book_id')
        book=Book.objects.get(id=book_id)
        bw=BookWishList.objects.get(book=book,user=request.user)
        bw.delete()
        return redirect('wishlist')

@login_required(redirect_field_name='login')
def show_cart(request):
    categories=Category.objects.all()
    ccart=CourseCart.objects.filter(user=request.user)
    bcart=BookCart.objects.filter(user=request.user)
    tcart=TestCart.objects.filter(user=request.user)
    btotal=0
    for b in bcart:
        btotal=btotal+b.total_price
    ctotal=0
    for c in ccart:
        ctotal=ctotal+c.course.course_price

    ttotal=0
    for t in tcart:
        ttotal=ttotal+t.test.price

    total_price=btotal+ctotal+ttotal
    tc=ccart.count()
    tb=bcart.count()
    tt=tcart.count()
    total_items=tc+tb+tt
    users=User.objects.all()
    return render(request,'app/shopping_cart.html',{'users':users,'ccart':ccart,'bcart':bcart,'tcart':tcart,'total_items':total_items,'categories':categories,'total_price':total_price})

@login_required(redirect_field_name='login')
def add_ccart(request):
    cid=request.GET['product']
    course=Course.objects.get(pk=cid)
    data={}
    checkc=CourseCart.objects.filter(course=course,user=request.user).count()
    checkw=CourseWishList.objects.filter(course=course,user=request.user)
    if checkc > 0:
        
        data={
            'string':'Items already added to cart'
        }
    else:
        CourseCart.objects.create(
            course=course,
            user=request.user
        )
        if checkw:
            checkw.delete()
        data={
            'string':'Item added to cart successfully'
        }
    return JsonResponse(data)

@login_required(redirect_field_name='login')
def add_bcart(request):
    bid=request.GET['product']
    book=Book.objects.get(pk=bid)
    qty=request.GET['qty']
    
    
    
    data={}
    checkc=BookCart.objects.filter(book=book,user=request.user).count()
    checkw=BookWishList.objects.filter(book=book,user=request.user)
    
    if checkc > 0:
        
        data={
            'string': 'Item already added to cart'
        }
    else:
        BookCart.objects.create(
            book=book,
            user=request.user,
            qty=qty,
            
        )
        if checkw:
            checkw.delete()
        data={
            'string': 'Item added to cart successfully'
        }
    return JsonResponse(data)

@login_required(redirect_field_name='login')
def add_tcart(request):
    tid=request.GET['product']
    test=MockTest.objects.get(pk=tid)
      
    
    
    data={}
    checkc=TestCart.objects.filter(test=test,user=request.user).count()
    checkw=TestWishList.objects.filter(test=test,user=request.user)
    
    if checkc > 0:
        
        data={
            'string': 'Item already added to cart'
        }
    else:
        TestCart.objects.create(
            test=test,
            user=request.user,
                        
        )
        if checkw:
            checkw.delete()
        data={
            'string': 'Item added to cart successfully'
        }
    return JsonResponse(data)

@login_required(redirect_field_name='login')
def delete_ccart(request,pk):        
    course=Course.objects.get(id=pk)
    cc=CourseCart.objects.get(course=course,user=request.user)
    cc.delete()
    return redirect('show_cart')

@login_required(redirect_field_name='login')
def delete_tcart(request,pk):        
    test=MockTest.objects.get(id=pk)
    tc=TestCart.objects.get(test=test,user=request.user)
    tc.delete()
    return redirect('show_cart')

@login_required(redirect_field_name='login')
def delete_bcart(request,pk):  
    book=Book.objects.get(id=pk)
    bc=BookCart.objects.get(book=book,user=request.user)
    bc.delete()
    return redirect('show_cart')

@login_required(redirect_field_name='login')
def delete_cart(request):  
    
    bc=BookCart.objects.filter(user=request.user)
    bc.delete()
    cc=CourseCart.objects.filter(user=request.user)
    cc.delete()
    return redirect('show_cart')

@login_required(redirect_field_name='login')
def total_cart(request):  
    
    bc=BookCart.objects.filter(user=request.user).count()
    
    cc=CourseCart.objects.filter(user=request.user).count()

    tc=TestCart.objects.filter(user=request.user).count()
    total_cart=bc+cc+tc
    return JsonResponse(total_cart,safe=False)

@login_required(redirect_field_name='login')
def checkout(request):    
    ccart=CourseCart.objects.filter(user=request.user)
    for c in ccart:
        MyCourse.objects.create(user=request.user,course=c.course,instructor=c.course.instructor_id)
        c.delete()

    tcart=TestCart.objects.filter(user=request.user)
    for t in tcart:
        MyMockTest.objects.create(user=request.user,mocktest=t.test)
        t.delete()

    bcart=BookCart.objects.filter(user=request.user)
    for b in bcart:
        bid=''+'qty'+str(b.book.id)
        qty=request.POST.get(bid)
    
        MyBooks.objects.create(user=request.user,book=b.book,qty=qty)
        b.delete()
    
    return render(request,'app/success.html')



def author_profile(request,pk):
    author=Author.objects.get(pk=pk)
    author_books=Book.objects.filter(author_id=author)
    categories=Category.objects.all()
    users=User.objects.all()
    return render(request,'app/author_profile.html',{'users':users,'author':author,'author_books':author_books,'categories':categories})


def instructor_profile(request,pk):
    instructor=Instructor.objects.get(pk=pk)
    categories=Category.objects.all()
    users=User.objects.all()
    return render(request,'app/author_profile.html',{'users':users,'instructor':instructor,'categories':categories})

@login_required(redirect_field_name='login')
def course_playlist(request,pk):
    course=Course.objects.get(pk=pk)
    # if id is not None:
    #     lesson=Lesson.objects.get(id=id)
    # else:
    #     lesson=Lesson.objects.filter(course_id=course).first()
    
    chapters=Chapter.objects.filter(course_id=course).order_by("chapter_position") 
    lessons=Lesson.objects.filter(course_id=course).order_by("lesson_position")
    categories=Category.objects.all()
    svideo=[]
    sassignment=[]
    squiz=[]
    studentVideo=StudentVideo.objects.filter(course=course,user=request.user)
    for s in studentVideo:
        svideo.append(s.lesson.id)
    studentAssignment=StudentAssignment.objects.filter(course=course,user=request.user)
    for a in studentAssignment:
        sassignment.append(a.lesson.id)
    studentQuiz=StudentQuiz.objects.filter(course=course,user=request.user)
    for q in studentQuiz:
        squiz.append(q.lesson.id)
    
    if request.method == 'POST':
        pk=request.POST.get('lesson_id')
        l=Lesson.objects.get(pk=pk)
        StudentAssignment.objects.get_or_create(course=course,lesson=l,user=request.user,instructor=course.instructor_id)
        afile=request.FILES.get('afile')
        sa=StudentAssignment.objects.filter(course=course,lesson=l,user=request.user)
        sa.update(assignment_file=afile)      
            
    users=User.objects.all()
    return render(request,'app/course_playlist.html',{'users':users,'categories':categories,'chapters':chapters,'lessons':lessons,'svideo':svideo,'sassignment':sassignment,'squiz':squiz,'studentAssignment':studentAssignment,'studentQuiz':studentQuiz})

@login_required(redirect_field_name='login')
def course_playlist_json(request):
    pk=request.GET['lesson_id']
    
    lesson=Lesson.objects.get(pk=pk)
    course=Course.objects.get(id=lesson.course_id.id)
    serializer=LessonSerializer(lesson)
    if lesson.lesson_type == 'V':
        StudentVideo.objects.get_or_create(course=course,lesson=lesson,user=request.user)
        
    # StudentAssignment.objects.filter(lesson=lesson,user=request.user).update(is_completed=True)
    
    # course=Course.objects.get(pk=pk)  
    # chapters=list(Chapter.objects.filter(course_id=lesson.course_id).order_by("chapter_position").values())
    # lessons=list(Lesson.objects.filter(course_id=lesson.course_id).values())
    
    return JsonResponse(serializer.data)
   
    
    
    
    
    


@login_required(redirect_field_name='login')
def mcq_json(request):
    pk=request.GET['lesson_id']
    
    lesson=Lesson.objects.get(pk=pk)
    quizes=list(Quiz.objects.filter(lesson=lesson).order_by('quiz_position').values())
    lserializer=LessonSerializer(lesson)
    
    
    
    return JsonResponse({'lesson':lserializer.data,'quizes':quizes})


@login_required(redirect_field_name='login')
def submit_quiz(request):
    pk=request.GET['lesson_id']
    mark=request.GET['mark']
    lesson=Lesson.objects.get(pk=pk)
    course=Course.objects.get(id=lesson.course_id.id)
    StudentQuiz.objects.create(user=request.user,course=course,lesson=lesson,quiz_mark=mark)
    return JsonResponse('Quiz Submitted Successully')

    
    
    
@login_required(redirect_field_name='login')
@csrf_exempt
def uploadFile(request):
    file=request.FILES.get('lesson_video')
    TempFile.objects.create(user=request.user,file=file)
    return JsonResponse('File Uploaded Successully',safe=False)