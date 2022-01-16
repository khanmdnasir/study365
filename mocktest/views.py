from django.shortcuts import render
from app.models import Category
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http.response import JsonResponse

def mocktests(request):
    search_query=request.GET.get('search')
    checkboxs=request.GET.getlist('checkbox')
    try:
        rate=int(request.GET.get('flexRadioDefault'))
    except:
        rate=''
    price=request.GET.get('price')
    page_number=request.GET.get('page')
    mocktests=MockTest.objects.all().order_by('id')
    
    if search_query != '' and search_query is not None:
        mocktests=mocktests.filter(title__icontains=search_query)
    
    if checkboxs:
        mocktests=mocktests.filter(category__in=checkboxs)
        
    if rate != 'None' and rate != '':
        filter_id = [x.id for x in MockTest.objects.all() if x.mocktest_rating == rate]

        mocktests=mocktests.filter(id__in=filter_id)
    
    if price != 'None' and rate != '':
        if price == 'free':
            mocktests=mocktests.filter(price = 0)

        if price == 'premium':
            mocktests=mocktests.filter(price != 0)
    
        
    paginator=Paginator(mocktests,45)
    
    page_obj=paginator.get_page(page_number)
    
    categories=Category.objects.all()
    
    num_of_test=len(mocktests)
    mwishlist=[]
    if request.user.is_authenticated:
        mw=TestWishList.objects.filter(user=request.user)
        for m in mw:
            mwishlist.append(m.test)
    
    users=User.objects.all()
    return render(request,'mocktest/mockTestAll.html',{'users':users,'categories':categories,'page_obj':page_obj,'num_of_test':num_of_test,'twishlist':mwishlist})

def mockTestDetails(request,id):
    mocktest=MockTest.objects.get(id=id)
    testset=TestSet.objects.filter(mocktest=mocktest)
    mtrating=MockTestRating.objects.filter(mocktest=mocktest)
    
    mwishlist=[]
    if request.user.is_authenticated:
        mw=TestWishList.objects.filter(user=request.user)
        for m in mw:
            mwishlist.append(m.test)

    users=User.objects.all()
    return render(request,'mocktest/mocktestDesc.html',{'users':users,'test':mocktest,'testset':testset,'mtrating':mtrating,'twishlist':mwishlist})


@login_required(redirect_field_name='login')
def mytests(request):
    mytests=MyMockTest.objects.filter(user=request.user)
    t_active='active'
    categories=Category.objects.all()
    users=User.objects.all()
    return render(request,'mocktest/stdPmyTest.html',{'users':users,'t_active':t_active,'categories':categories,'mytests':mytests})

@login_required(redirect_field_name='login')
def myTestDes(request,id):
    mocktest=MockTest.objects.get(id=id)
    is_retake=[]
    mytestset=MyTestSet.objects.filter(user=request.user,mocktest=mocktest)
    for mt in mytestset:
        if mt.is_completed:
            is_retake.append(mt.testset.id)
    testset=TestSet.objects.filter(mocktest=mocktest)
    mtrating=MockTestRating.objects.filter(mocktest=mocktest)
    categories=Category.objects.all()
    users=User.objects.all()
    t_active='active'
    
    return render(request,'mocktest/stdPmyTestDes.html',{'t_active':t_active,'users':users,'test':mocktest,'testset':testset,'mtrating':mtrating,'categories':categories,'is_retake':is_retake})


@login_required(redirect_field_name='login')
def startTest(request):
    id=request.GET.get('tid')
    mid=request.GET.get('mid')
    testset=TestSet.objects.get(id=id)
    mocktest=MockTest.objects.get(id=mid)
    questions=TestQuestion.objects.filter(testset=testset)
    categories=Category.objects.all()
    users=User.objects.all()
    
    if MyTestSet.objects.filter(user=request.user,mocktest=mocktest,testset=testset).exists():
        mytest=MyTestSet.objects.get(user=request.user,mocktest=mocktest,testset=testset)
    else:
        mytest=MyTestSet.objects.create(user=request.user,mocktest=mocktest,testset=testset)

    if mytest.is_completed == True:
        mytest.is_completed = False
        mytest.time = 30
        mytest.save()
    
    if request.method == 'POST':
        correct=0
        for q in questions:
            
            qid=request.POST.get(f'q{q.id}')
            question=TestQuestion.objects.get(id=qid)
            answer=request.POST.get(f'group{q.id}')
            if answer == question.correct:
                correct+=1
            if UserTest.objects.filter(mytest=mytest,question=question).exists():
                UserTest.objects.filter(mytest=mytest,question=question).update(answer=answer)
            else:
                UserTest.objects.create(mytest=mytest,question=question,answer=answer)
            
        mytest.total_mark=correct
        mytest.is_completed=True
        mytest.save()               
        users=User.objects.all()
        return render(request,'mocktest/mockTestAcheivement.html',{'users':users,'mytest':mytest,'categories':categories})

    return render(request,'mocktest/mockTestStart.html',{'users':users,'testset':testset,'questions':questions,'categories':categories,'mytest':mytest})

@login_required(redirect_field_name='login')
def viewresult(request,id):
    mytest=MyTestSet.objects.get(id=id)
    usertest=UserTest.objects.filter(mytest=mytest)
    categories=Category.objects.all()
    users=User.objects.all()
    return render(request,'mocktest/mockTestViewRslt.html',{'users':users,'categories':categories,'usertest':usertest})


@login_required(redirect_field_name='login')
def timeCount(request):
    id=request.GET['id']
    time=request.GET['time']
    MyTestSet.objects.filter(id=id).update(time=time)
    return JsonResponse('Time Updated Successully',safe=False)

