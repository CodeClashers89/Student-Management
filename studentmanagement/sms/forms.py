from django import forms
from .models import CustomUser,Student,Faculty,TestExam,Result,Subjects

class StudentRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150,required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)

    class Meta:
        model= Student
        fields = ['date_of_birth','gender','father_name','father_contact_no','father_email','address','branch',
              'aadhar_no','is_tfws','cast_catogry','admission_through','level','admission_heads','photo_student',
              'leaving_certificate']
    