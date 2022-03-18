from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db.models.fields import CharField
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from payu.models import Transaction
from django.shortcuts import reverse
from django.utils.text import slugify

# Create your models here.


highest_qualification_choices = (
    ("No formal education", "No formal education"),
    ("Primary Education", "Primary Education"),
    ("Secondary Education", "Secondary Education"),
    ("Bachelor's Degree", "Bachelor's Degree"),
    ("Master's Degree", "Master's Degree"),
)


class MyAccountManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, phone, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not phone:
            raise ValueError("Users must have a phone number")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, phone, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


type1 = (
    ("regular", "Regular"),
    ("franchise", "Franchisee"),

)

choices2 = (("Male", "Male"), ("female", "Female"), ("other", "Other"))


class Account(AbstractBaseUser):

    first_name = models.CharField(verbose_name="First Name", max_length=30)
    last_name = models.CharField(verbose_name="Last Name", max_length=30)
    email = models.EmailField(verbose_name="Email", max_length=70, unique=True)
    type = models.CharField(
        choices=type1, default="Regular", null=True, max_length=30)
    phone = PhoneNumberField(
        help_text='Enter valid contact number with country code')
    country = CountryField(null=True, blank_label="Choose Country")
    dob = models.DateField(verbose_name="Date of Birth",
                           max_length=8, null=True)
    hq = models.CharField(max_length=50, verbose_name="Highest Qualification",
                          null=True, choices=highest_qualification_choices)
    pro_pic = models.ImageField(null=True, blank=True, verbose_name='Profile Picture',
                                default='default_pic.jpg', upload_to='profile_pictures')
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True, verbose_name='Email Verification')
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    transactions = models.ManyToManyField(Transaction, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


choices3 = (("Micro Category Multirotor Drone Pilot Course", "Micro Category Multirotor Drone Pilot Course"), ("Small Category Multirotor Drone Pilot Course",
            "Small Category Multirotor Drone Pilot Course"), ('Micro Category Fixedwing Drone Pilot Course', 'Micro Category Fixedwing Drone Pilot Course'))

choices4 = (('voter id', 'voter id '), ('Aadhar no', 'Aadhar no'))


class PilotCertificates(models.Model):
    name = models.CharField(verbose_name="Student Name", max_length=100)
    sex = models.CharField(verbose_name="Gender", max_length=30, choices=choices2)
    Dob = models.CharField(verbose_name="Date of Birth", max_length=200, blank=True)
    Address = models.CharField(max_length=250)
    Photo_ID_detail = models.CharField(
        verbose_name="Photo ID Type", max_length=100, choices=choices4, default="voter id")
    Photo_ID = models.CharField(verbose_name="Photo ID Number", max_length=100)
    photo = models.ImageField(verbose_name="Photo ID Image", upload_to='images/')
    certificate_number = models.CharField(
        verbose_name="Certificate Number", max_length=200)
    dateofissue = models.CharField(verbose_name="Date of Issue", max_length=200, default="", blank=True)
    category = models.CharField(max_length=200, choices=choices3)
    price = models.BigIntegerField(verbose_name="Fee Collected", null=True, blank=True)
    completed = models.BooleanField(verbose_name="Form Completed", default=False)
    slug = models.SlugField(null=True, blank=True)
    valid_date = models.CharField(max_length=100, null=True, blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
            verbose_name = 'Pilot Certificate'
            verbose_name_plural = 'Pilot Certificates'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        # if self.category:
        #     if self.category == 'Micro Category Fixedwing Drone Pilot Course':
        #         self.price = 30

        #     elif self.category == 'Small Category Multirotor Drone Pilot Course':
        #         self.price = 40

        #     elif self.category == 'Micro Category Multirotor Drone Pilot Course':
        #         self.price = 50

        self.slug = slugify(str(self.id))

        super(PilotCertificates, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("account:products1", kwargs={"slug": self.slug})

    def show(self):
        return reverse("account:proceed1", kwargs={"slug": self.slug})


class FranchiseeOwners(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    Total_batch = models.CharField(max_length=10)
    total_certificate = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    certificate_students = models.ManyToManyField(
        PilotCertificates, null=True, blank=True)

    class Meta:
            verbose_name = 'Franchisee Owner'
            verbose_name_plural = 'Franchisee Owners'

    def __str__(self):
        return self.user.email



