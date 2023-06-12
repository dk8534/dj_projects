from django.shortcuts import render
from .models import filter_model
# Create your views here.

def filter_view(request):
    obj = filter_model.objects.all()
    context = {
        'obj' : obj
    }
    return render(request,'home.html',context)