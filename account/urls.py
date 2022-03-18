from . import views
from django.urls import path
from django.conf.urls import url
from .views import Proceed,changeaddress,franchiseportal,certificategen,check1,show,certificate_numberss,Proceed1, subscription ,subscriptioncheck

app_name = 'account'

urlpatterns = [
     path('profile/', views.profile_view, name="profile"),
     path('mycourses/', views.MyCourses, name='mycourses'),
     path('lesson_list/<slug>/', views.LessonList, name="lesson_list"),
     path('activate/<uidb64>/<token>', views.activate,
         name='activate'),
     path('add_address',Proceed,name="address"),
     path('changeaddress',changeaddress,name="changeaddress"),
     path('franchise/',franchiseportal,name="franchise"),
     path('certificategen',certificategen,name="certificate"),
     path('check1',check1,name="check1"),
    path('show',show,name="show"),
    # path('certificate_number1/<slug:slug>',certificate_number1,name="certificate_number1"),
    path('acc/<slug:slug>',certificate_numberss,name="products1"),
    path('acc1/<slug:slug>',Proceed1,name="proceed1"),
    path('sub',subscription,name="subscription"),
    path('subscrip/<slug:slug>/',subscriptioncheck,name="subscrip")
    
]
