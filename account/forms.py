from django.forms import ModelForm, Textarea
from app.models import Item
from django.forms.widgets import DateInput
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django.contrib.auth import authenticate
from phonenumber_field import formfields, widgets
from PIL import Image


highest_qualification_choices = (
    ("No formal education", "No formal education"),
    ("Primary Education", "Primary Education"),
    ("Secondary Education", "Secondary Education"),
    ("Bachelor's Degree", "Bachelor's Degree"),
    ("Master's Degree", "Master's Degree"),
)


class SignUpForm(UserCreationForm):
    phone = formfields.PhoneNumberField(
        widget=widgets.PhoneNumberPrefixWidget(), initial='+91')

    class Meta:
        model = Account
        # Fields while signing up through the website
        fields = ('email', 'first_name', 'last_name', 'phone')


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                # print('Not authenticated')
                raise forms.ValidationError("Invalid Details")

            # if email and password:
            #     user = authenticate(username = email, password = password)
            #     if not user:
            #         raise forms.ValidationError("This user does not exist..")
            #
            #     if not user.check_password(password):
            #         raise forms.ValidationError("Incorrect password...")
            #
            #     if not user.is_active:
            #         raise forms.ValidationError("This user does not appear to be active.")


class ProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1920, 2020)), label="Date of Birth")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hq'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['dob'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Account
        fields = ('country', 'dob', 'hq', 'pro_pic')


choices2 = (("Male", "Male"), ("female", "Female"), ("other", "Other"))

choices3 = (("Micro Category Multirotor Drone Pilot Course", "Micro Category Multirotor Drone Pilot Course"), ("Small Category Multirotor Drone Pilot Course",
            "Small Category Multirotor Drone Pilot Course"), ('Micro Category Fixedwing Drone Pilot Course', 'Micro Category Fixedwing Drone Pilot Course'))

choices4 = (('voter id', 'Voter ID '), ('Aadhar no', 'Aadhar Card'),
            ('Passport', 'Passport'), ('driving licence','Driving License'))


class certificate_form(forms.Form):
    name = forms.CharField(label="Student Name", max_length=100)
    Address = forms.CharField(max_length=250)
    dob = forms.DateField(label="Date of Birth",
                          widget=DateInput(attrs={'type': 'date'})
                          )
    Photo_ID = forms.CharField(
        label="Photo ID Type", max_length=100, widget=forms.Select(choices=choices4))
    blank = forms.CharField(label="Photo ID Number",
                            max_length=50)
    sex = forms.CharField(
        label='Gender', widget=forms.Select(choices=choices2))
    category = forms.CharField(
        label="Select the Course Name", widget=forms.Select(choices=choices3))
    # category = forms.ModelChoiceField(queryset=Item.objects.all())
    img = forms.ImageField(label="Upload Student Image",
                           help_text="Resolution of the Image must be")

    def clean(self):

        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("img")
        myself = cleaned_data.get("name")
        subject = cleaned_data.get("Address")

        w, h = get_image_dimensions(cc_myself)

        print(w, h)
        if not (w > 200 or w <= 500):

            msg = "width error"
            self.add_error('img', msg)

        if not(h >= 200 or h <= 500):

            msg = "height error "
            self.add_error('img', msg)
