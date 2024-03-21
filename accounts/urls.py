from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("signin/",views.signin_sys,name='signin'),
    path("signup/",views.signup_sys,name='signup'),
    path("signout/",views.signout,name='signout'),
    path("signin_faild/",views.signin_faild,name='signin_faild'),
    path("signup_faild/",views.signup_faild,name='signup_faild'),
]