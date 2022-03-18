from django.forms import ModelForm, fields
from .models import Job,student_apply
from django import forms


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'created_at',)

    def is_valid(self):
        valid = super(CreateJobForm, self).is_valid()
        
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        if commit:
            job.save()
        return job

class studentaplyforms(forms.ModelForm):
    class Meta:
        model=student_apply
        fields = "__all__"
        exclude = ('student_profile',)



