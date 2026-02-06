from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CustomUser,Student,Faculty,Subjects,Result,TestExam
from .forms import StudentRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'student/student_dashboard.html')

def login(request):
    return render(request, 'login.html')

def newtest(request):
    return render(request, 'student/newtest.html')

def profile(request):
    return render(request, 'teacher/profile.html')

def result(request):
    return render(request, 'student/result.html')

<<<<<<< HEAD
def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
    else:
        form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'form':form})
    
=======
def test(request):
    return render(request, 'teacher/teacher_dashboard.html')
>>>>>>> 36730d4e1b70069855346ebc3c1ad78a8ea46b22
