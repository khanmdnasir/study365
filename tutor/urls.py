from django.urls import path
from . import views
app_name='tutor'
urlpatterns = [
    path('dashboard/',views.tutor_dashboard,name='tutor_dashboard'),
    path('signin/',views.tutor_signin,name='tutor_signin'),
    path('signup/',views.tutor_signup,name='tutor_signup'),
    path('profile/',views.tutor_profile,name='tutor_profile'),
    path('addcourse/',views.addCourse,name='addCourse'),
    path('addChapter/<int:id>',views.addChapter,name='addChapter'),
    path('addLesson/<int:id1>/<int:id2>',views.addLesson,name='addLesson'),
    path('addQuiz/<int:id>',views.addQuiz,name='addQuiz'),
    path('editQuiz/<int:id>',views.editQuiz,name='editQuiz'),
    path('deleteQuiz/<int:id>',views.deleteQuiz,name='deleteQuiz'),
    path('editCourse/<int:id>',views.editCourse,name='editCourse'),
    path('deleteCourse/<int:id>',views.deleteCourse,name='deleteCourse'),
    path('editChapter/<int:id>',views.editChapter,name='editChapter'),
    path('deleteChapter/<int:id>',views.deleteChapter,name='deleteChapter'),
    path('editLesson/<int:id>',views.editLesson,name='editLesson'),
    path('deleteLesson/<int:id>',views.deleteLesson,name='deleteLesson'),
    path('mycourse/',views.myCourse,name='myCourse'),
    path('singleCourse/<int:id>',views.singleCourse,name='singleCourse'),
    path('coursePublish/<int:id>',views.coursePublish,name='coursePublish'),
    path('mystudents/',views.myStudents,name='myStudents'),
    path('allsubmission/',views.allSubmission,name='allSubmission'),
    path('guidelines/',views.guidelines,name='guidelines'),
    path('help&support/',views.helpSupport,name='helpSupport'),
    path('payment/',views.payment,name='payment'),
    path('settings/',views.settings,name='settings'),    
    
    
   
]