from django.shortcuts import render
from .models import Subject, Block, Options

# Create your views here.

def landingpage(request):
    return render(request, 'index.html')

def control(request):
    subject = Subject.objects.only('name', 'description')
    return render(request, 'admin.html', {'subject': subject})

def student(request):
    return render(request, 'student.html')

