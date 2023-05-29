from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def bollywood(request):
    return render(request,'bollywood.html')

def hollywood(request):
    return render(request,'hollywood.html')

def political(request):
    return render(request,'political.html')

def sports(request):
    return render(request,'sports.html')

def bussiness(request):
    return render(request,'bussiness.html')

def brand(request):
    return render(request,'brand.html')

