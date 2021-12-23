from django.shortcuts import render
from app.models import Category
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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
            mocktests=mocktests.filter(price is not 0)
    
        
    paginator=Paginator(mocktests,45)
    
    page_obj=paginator.get_page(page_number)
    
    categories=Category.objects.all()
    
    num_of_test=len(mocktests)
    mwishlist=[]
    if request.user.is_authenticated:
        mw=TestWishList.objects.filter(user=request.user)
        for m in mw:
            mwishlist.append(m.test)
    return render(request,'mocktest/mockTestAll.html',{'categories':categories,'page_obj':page_obj,'num_of_test':num_of_test,'twishlist':mwishlist})

def mockTestDetails(request,id):
    mocktest=MockTest.objects.get(id=id)
    testset=TestSet.objects.filter(mocktest=mocktest)
    mtrating=MockTestRating.objects.filter(mocktest=mocktest)
    mwishlist=[]
    if request.user.is_authenticated:
        mw=TestWishList.objects.filter(user=request.user)
        for m in mw:
            mwishlist.append(m.mocktest)
    return render(request,'mocktest/mocktestDesc.html',{'test':mocktest,'testset':testset,'mtrating':mtrating,'twishlist':mwishlist})


@login_required(redirect_field_name='login')
def mytests(request):
    mytests=MyMockTest.objects.filter(user=request.user)
    t_active='active'
    categories=Category.objects.all()
    return render(request,'mocktest/stdPmyTest.html',{'t_active':t_active,'categories':categories,'mytests':mytests})

@login_required(redirect_field_name='login')
def myTestDes(request,id):
    mocktest=MockTest.objects.get(id=id)
    testset=TestSet.objects.filter(mocktest=mocktest)
    mtrating=MockTestRating.objects.filter(mocktest=mocktest)
    categories=Category.objects.all()
    return render(request,'mocktest/stdPmyTestDes.html',{'test':mocktest,'testset':testset,'mtrating':mtrating,'categories':categories})


@login_required(redirect_field_name='login')
def startTest(request):
    id=request.GET.get('tid')
    testset=TestSet.objects.get(id=id)
    questions=TestQuestion.objects.filter(testset=testset)
    categories=Category.objects.all()
    if request.method == 'POST':
        correct=0
        for q in questions:
            
            qid=request.POST.get(f'q{q.id}')
            question=TestQuestion.objects.get(id=qid)
            answer=request.POST.get(f'group{q.id}')
            if answer == question.correct:
                correct+=1
            UserTest.objects.update_or_create(user=request.user,testset=testset,question=question,answer=answer)
        MyTestSet.objects.update_or_create(user=request.user,testset=testset,total_mark=correct)
        mytest=MyTestSet.objects.get(testset=testset)
        print(mytest.total_mark)
        return render(request,'mocktest/mockTestAcheivement.html',{'mytest':mytest,'categories':categories})
    return render(request,'mocktest/mockTestStart.html',{'questions':questions,'categories':categories})

@login_required(redirect_field_name='login')
def viewresult(request,id):
    testset=TestSet.objects.get(id=id)
    usertest=UserTest.objects.filter(testset=testset)
    categories=Category.objects.all()
    return render(request,'mocktest/mockTestViewRslt.html',{'categories':categories,'usertest':usertest})

