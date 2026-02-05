from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'student/student_dashboard.html')

def login(request):
    return render(request, 'login.html')

def newtest(request):
    return render(request, 'student/newtest.html')