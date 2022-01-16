from django.urls import path
from . import views
app_name='mocktest'
urlpatterns = [
      path('',views.mocktests,name="mocktests"),
      path('mock_test_details/<int:id>',views.mockTestDetails,name="mockTestDetails"),
      path('my_tests',views.mytests,name="mytests"),
      path('my_test_des/<int:id>',views.myTestDes,name="myTestDes"),
      path('start_test/',views.startTest,name="startTest"),
      path('view_result/<int:id>',views.viewresult,name="viewresult"),
      path('timeCount/',views.timeCount),
      
]