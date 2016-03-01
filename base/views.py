from django.shortcuts import render
from django.shortcuts import render_to_response
from base.models import BlogEntry

def index(request):
    data =  BlogEntry.objects.last()
    return render_to_response('index.html',{'data':data})

def blog(request,id):
    data =  BlogEntry.objects.filter(id=id)[0]
    return render_to_response('entry.html',{'data':data})

# Create your views here.
