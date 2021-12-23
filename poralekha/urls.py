from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from users import views

# from users import ApiView
from users.forms import AuthenticationForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
#     path('auth/', include('djoser.urls')),
#     path('auth/', include('djoser.urls.jwt')),
    path('',include('app.urls')),
    path('tutor',include('tutor.urls',namespace='tutor')),
    path('accounts/', include('allauth.urls')),
    path('mocktest/', include('mocktest.urls',namespace='mocktest')),
    path('accounts/password_change',PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPasswordChangeForm),name="changepassword"),
    path('accounts/password_change/done',PasswordChangeDoneView.as_view(template_name='app/passChangeDone.html'),name="password_change_done"),
    path('accounts/password_reset/',PasswordResetView.as_view(template_name="app/password_reset.html",form_class=MyPasswordResetForm),name="password_reset"),
    path('accounts/password_reset/done/',PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"),name="password_reset_done"),
    path('accounts/reset/done/',PasswordResetCompleteView.as_view(template_name="app/password_reset_complete.html"),name="password_reset_complete"),
    path('accounts/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html",form_class=MySetPasswordForm),name="password_reset_confirm"),
    
    path('login/',views.login_view,name='login'),
    # path('accounts/login/', LoginView.as_view(template_name='app/login.html',authentication_form=AuthenticationForm), name='login'),
    path('accounts/logout/',LogoutView.as_view(),name='logout'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.registration_view, name='registration'),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
        
    path('verify/',views.verify_view,name='verify'),
    path('verify_st_tutor/',views.verify_view1,name='verify1'),
    path('student/profile/',views.stdprofile_view,name='stdprofile'),
    path('student/profile/edit/',views.edit_profile,name='edit_profile'),
    
    path('profile/account_settings/',views.account_settings,name='account_settings'),
    path('profile/account_settings/change_phone/',views.change_phone,name='change_phone'),
    path('profile/account_settings/change_email/',views.change_email,name='change_email'),
    
    path('summernote/', include('django_summernote.urls')),
#     api urls
    #  path('api/registration/',ApiView.RegisterApi)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
