from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Student
import razorpay
# Create your views here.
def indexView(request):
    return render(request,'index.html')
@login_required
def dashboardView(request):
    student = Student.objects.all()
    print(student)
    client = razorpay.Client(auth=("rzp_live_WmyvJGcwPFpcgQ", "h4Scm4v6aUIeLjs1iS6ePimt"))
    return render(request,'dashboard.html',{"messages":student})

def get(self, request):
    student = Student.objects.all()
    print(student)
    return render(request,self.template_name)

def course1(request):
    return render(request,'course1.html')

def registerView(request):
    if request.method == "POST":
        username=request.username
        form = UserCreationForm(request.POST)
        if form.is_valid():
               form.save()
               return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})
