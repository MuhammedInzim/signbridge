"""
URL configuration for Hands2Hope project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',loginview.as_view(), name='login'),
    path('manage_users',manageuser.as_view(),name='manage_users'),
    path('feedback',feedback.as_view(),name='feedback'),
    path('complaints',complaints.as_view(),name='complaints'),
    path('adminhompage',adminhomepage.as_view(),name='adminhompage'),
    path('userhomepage',userhomepage.as_view(),name='userhomepage'),
    path('Replyview/<int:id>',Replyview.as_view(),name='Replyview'),
    path('delete/<int:id>',DeleteUser.as_view()),
    path('usercomplaints',usercomplaints.as_view(),name='usercomplaints'),
    path('userfeedback',userfeedback.as_view(),name='userfeedback'),
    path('user_registration',userregistration.as_view(),name='user_registration'),
    path('viewcomplaints',viewcomplaints.as_view(),name='viewcomplaints'),
    path('viewfeedback',viewfeedback.as_view(),name='viewfeedback'),
    path('isl_page',isl_page.as_view(),name='isl_page'),
    path('video_feed',video_feed.as_view(),name='video_feed'),
    path('StartSignAnimationView',StartSignAnimationView.as_view(),name='StartSignAnimationView'),
    path('Profilesview/',Profilesview.as_view(), name='profile'),
    path('editprof/<int:id>/',edituser.as_view(), name='editprofile'),
    path('Forgotpassword',ForgetPassword.as_view(), name='ForgetPassword'),
    path('signs',signs.as_view(), name='signs'),

]