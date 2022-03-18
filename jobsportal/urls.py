from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic import TemplateView
app_name = 'jobportal'


urlpatterns = [
   

  path('post/<slug>',Post1,name="Post1"),
  path('createstudent',createstudent,name="createstudent"),
  path('create',check_current_account,name="checkcurrent"),
  path('allcategory',allcategory_all,name="allcategory"),
  path('modeldetail1/<pk>',modeldetail1category,name="modeldetail1"),
  path('updateprofile',updateprofile,name="updateprofile"),
  path('temp', TemplateView.as_view(template_name="notify.html"),name="notify"),
  path('',filter,name="filter"),
  path('student_apply1/<pk>',student_apply1,name="student_apply1")

]
