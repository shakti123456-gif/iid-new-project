from django.db import models
from django.db.models.base import Model

from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from account.models import Account

membership_CHOICES=(

('Free','Free'),('Monthly','Monthly'),('Year','Year')

)

class membership(models.Model):
    
    slug=models.SlugField()
    membership_type=models.CharField(

        choices=membership_CHOICES,
        default='Free',
        max_length=30
    )
    price=models.IntegerField(default=0)

    def __str__(self) :
        return self.membership_type
    

    def save(self,*args,**kwargs):
        self.slug = slugify(self.membership_type) 
        return super(membership, self).save(*args, **kwargs)
    

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})
    

from django.dispatch import receiver
from django.db.models.signals import pre_save

state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

class allcategory(models.Model):
    name=models.CharField(max_length=200)
    description1=models.CharField(max_length=200,default="")
    description2=models.CharField(max_length=200,default="")
    img=models.ImageField(default="s4.jpg")
    zone=models.CharField(max_length=200,choices=state_choices,null=True,blank=True)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("jobportal:modeldetail1", kwargs={"pk": self.pk})
    
  

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    type = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    company_description = models.CharField(max_length=300,null=True,blank=True)
    website = models.CharField(max_length=100, default="")
    
 
    def __str__ (self):
        return self.company_name

from django.template.defaultfilters import default, slugify
from django.urls import reverse

class Job(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    location = models.CharField(max_length=150,null=True,blank=True)
    type = models.CharField(choices=JOB_TYPE, max_length=10,null=True,blank=True)
    last_date = models.DateTimeField(null=True,blank=True)
    Campny = models.ForeignKey(Company, null=True,blank=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)
    slug=models.SlugField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.pk) 
        return super(Job, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("jobportal:Post1", kwargs={"slug": self.slug})
    
        

choice=(('1','0-1'),('2','1-2'),('3','2-3'))


choice1 = (
        ('West Zone', (
            ('WZ', 'Rajasthan '),
            ('WZ', 'Madhya Pradesh'),
            ('WZ', 'Gujarat'),
            ('WZ', 'Daman & Diu'),
            ('WZ', 'Dadra & Nagar Haveli '),
            ('WZ', 'Maharashtra'),
            ('WZ', 'Goa'),
        )),
        ('South Zone', (
            ('SZ', 'Andhra Pradesh'),
            ('SZ', 'Lakshadweep'),
            ('SZ', 'Kerala'),
            ('SZ', 'Tamil Nadu'),
            ('SZ', 'Andaman & Nicobar'),
        )),
        ('North Zone', (
            ('NZ', 'Jammu & Kashmir'),
            ('NZ', 'Himachal Pradesh'),
            ('NZ', 'Chandigarh'),
            ('NZ', 'Haryana '),
            ('NZ', 'Delhi'),
            ('NZ', 'Uttar Pradesh'),
        )),
        ('East Zone', (
            ('EZ', 'Bihar'),
            ('EZ', 'Sikkim'),
            ('EZ', 'Arunachal Pradesh'),
            ('EZ', 'Nagaland'),
            ('EZ', 'Manipur'),
            ('EZ', 'Meghalaya'),
            ('EZ', 'Assam'),
            ('EZ', 'West Bengal'),
            ('EZ', 'Jharkhand'),
            ('EZ', 'Odisha'),
            ('EZ', 'Chhattisgarh'),
        )),
        
    )

class student_apply(models.Model):
    student_profile=models.OneToOneField(Account, on_delete=models.CASCADE)
    Category=models.ForeignKey(allcategory, on_delete=models.CASCADE,null=True,blank=True)
    Experience=models.CharField(max_length=10,choices=choice)
    resume=models.FileField();  
    zone=models.CharField(max_length=200,choices=choice1,null=True,blank=True)

    def __str__(self):
        return str(self.student_profile)
    def get_absolute_url(self):
        return reverse("jobportal:student_apply1", kwargs={"pk": self.pk})
    

class Application(models.Model):
    profilename = models.CharField(max_length=200, default="",null=True,blank=True)
    students=models.ForeignKey(student_apply,on_delete=models.CASCADE,null=True,blank=True)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    apply_date = models.DateField(auto_now_add=True)
    
    def __str__ (self):
        return str(self.students.student_profile.email)



class UserMembership(models.Model):
    usermembership=models.ForeignKey(Account,on_delete=models.CASCADE)
    membership_method=models.ForeignKey(membership,on_delete=models.CASCADE)
    active=models.BooleanField(default=False)
    Application_apply=models.ManyToManyField(Application,null=True,blank=True)
    dateofaccount=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.usermembership.first_name + self.usermembership.last_name)
    
    def get_absolute_url(self):
        return reverse("jobportal:post2", kwargs={"pk": self.pk})


@receiver(pre_save,sender=UserMembership)
def checkmemebership(sender,instance,**kwargs):
    print("im triggering method")


