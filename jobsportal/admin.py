from django.contrib import admin

from jobsportal.models import Company

from .models import Company,Job,Application,student_apply,UserMembership,membership,allcategory

admin.site.register(Company)

admin.site.register(Job)

admin.site.register(Application)

admin.site.register(student_apply)

admin.site.register(UserMembership)

admin.site.register(membership)

admin.site.register(allcategory)