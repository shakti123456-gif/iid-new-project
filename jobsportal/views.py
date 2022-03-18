from django import http
from django.http.response import Http404, HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse, request
from django.template.defaultfilters import title
from django.views import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

def jobportalhome(request):  
    
    if request.method == "POST":
     
        s1=request.POST.get('id3')
        s2=request.POST.get('id3')

        jobs=Job.objects.filter(title=s1)
        print(jobs)

        job1=True
        context={'s3':s1,"job":jobs,'Job1':job1}

        print(s1)

        return render(request,"homejobs.html",context)        
    return render(request,'homejobs.html',{'job':False})


class GreetingView(View):
    
    def get(self, request):
        return HttpResponse(self.greeting)

    def post(self,request):
        return HttpResponse("this is working on day")

def search_box(request):
    
    return render(request,"request.html")


@login_required(login_url='/login/')
def Post1(request,slug):    

    specificjobs=Job.objects.filter(slug=slug)[0]
    member_specific=UserMembership.objects.filter(jobs_add=specificjobs).first()

    if request.method=='POST':
        try:
            student=student_apply.objects.filter(student_profile__email=request.user)[0]
          
            if student:
                ss=Application.objects.create(profilename=str(request.user),students=student,job=specificjobs)
                ss.save()
                # add error
                if member_specific.Application_apply.all().filter(profilename=ss.profilename).exists():
                    messages.success(request, 'already apply for this job')
                    return redirect("jobportal:jobportalhome")

                else:
                    member_specific.Application_apply.add(ss)
                    member_specific.save()
        
                
                messages.success(request, 'successfully  apply for this job')
                return redirect("jobportal:jobportalhome") 


            else:
                return redirect("jobportal:jobportalhome") 
        except:
            return redirect("jobportal:createstudent")    
        
        
        return render(request,"homejobs.html")
    
    return render(request,"specificjobs.html",{"jobsdesc":specificjobs ,"jobs":member_specific})



from .form import studentaplyforms

def createstudent(request):
    pass


def check_current_account(request):
    ss=UserMembership.objects.filter(UserMembership__email=request.user)[0]
    HttpResponse("this is my response",ss)


def allcategory_all(request):
    allentry=allcategory.objects.all()

    return render(request,"student_application.html",{'allentry':allentry})


def modeldetail1category(request,pk):
    student=student_apply.objects.filter(student_profile__email=request.user).first()
    print(student)
    s1=Account.objects.get(email=request.user)
    
    if student:
        if pk=="todo":
            messages.info(request,' update your account')
        else:
            messages.info(request,'you cannnot apply please update your account')
        return render(request,"application.html",{"s1":s1,"student":student})
    else:
        studentform=studentaplyforms()
        if request.method=="POST":
            form = studentaplyforms(request.POST, request.FILES)
            if form.is_valid():
                Experience=form.cleaned_data['Experience']
                resume=form.cleaned_data['resume']
                Category=form.cleaned_data['Category']
                Zone=form.cleaned_data['zone']
                s1=Account.objects.get(email=request.user)
                studentformssave=student_apply.objects.create(student_profile=s1,Experience=Experience,resume=resume,Category=Category,zone=Zone)
                studentformssave.save()
            else:
                return Http404("error 404")
        return render(request,"studentinfo.html",{'student':studentform}) 

def updateprofile(request):
    studentform=studentaplyforms()
    if request.method=="POST":
        form = studentaplyforms(request.POST, request.FILES)
        if form.is_valid():
            Experience=form.cleaned_data['Experience']
            resume=form.cleaned_data['resume']
            Category=form.cleaned_data['Category']
            Zone=form.cleaned_data['zone']
            s1=Account.objects.get(email=request.user)
            studentformssave=student_apply.objects.get(student_profile=s1)
            studentformssave.Experience=Experience
            studentformssave.resume=resume
            studentformssave.Category=Category
            studentformssave.Zone=Zone 
            studentformssave.save()
            return redirect("jobportal:modeldetail1", pk='todo')
        else:
            return Http404("error 404")
    return render(request,"studentupdate.html",{'student':studentform}) 


def filter(request):
    user=UserMembership.objects.filter(usermembership__email=request.user).first()
    print(user)

    if user and  not (str(user.membership_method) == str('Free')):
        students=student_apply.objects.all()


    else:
        students=False
        return redirect("account:subscription")
        # return HttpResponseBadRequest("Bad request")

    return render(request,"filter.html",{'student_apply':students})

def student_apply1(request,pk):
    students=student_apply.objects.get(pk=pk)
    print(students)
    context={'students':students}
    return render(request,"studentdetail.html",context)