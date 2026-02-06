from django import forms
from .models import CustomUser,Student,Faculty,TestExam,Result,Subjects
from datetime import datetime,time,date

class StudentRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100,required=True)
    phone_no = forms.CharField(max_length = 15,required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150,required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)

    class Meta:
        model= Student
        fields = ['date_of_birth','gender','father_name','father_contact_no','father_email','address','branch',
              'aadhar_no','is_tfws','cast_catogry','admission_through','level','admission_heads','photo_student',
              'leaving_certificate'] 
        
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        # Create user first
        user = CustomUser.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            phone_no = self.cleaned_data['phone_no'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            role='Student'
        )

        student = super().save(commit=False)
        student.user = user
        if commit:
            student.save()
        return student
    
class FacultyRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(max_length = 15, required=True)
    username = forms.CharField(max_length=150,required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)

    class Meta:
        model= Faculty
        fields = ['date_of_birth','gender','address','department',
              'aadhar_no','salary','graduation_level', 'photo_faculty'] 
        
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        # Create user first
        user = CustomUser.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            phone_no = self.cleaned_data['phone_no'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            role='Faculty'
        )

        faculty = super().save(commit=False)
        faculty.user = user
        if commit:
            faculty.save()
        return faculty
    

class CreateTestForm(forms.ModelForm):
    class Meta:
        model = TestExam
        fields = ['test_date', 'syllabus', 'total_marks', 'duration', 'te_type', 'department', 'subject']
        widgets = {
            'test_date': forms.DateInput(attrs={'type': 'date'}),
            'syllabus': forms.Textarea(attrs={'rows':3}),
        }

    


