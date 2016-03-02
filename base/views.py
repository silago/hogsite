from django.shortcuts import render
from django.shortcuts import render_to_response
from base.models import BlogEntry, SceneFeature

def index(request):
    data =  BlogEntry.objects.last()
    return render_to_response('index.html',{'data':data})

def blog(request,id):
    data =  BlogEntry.objects.filter(id=id)[0]
    return render_to_response('entry.html',{'data':data})

def scenes_features(request):
    data =  SceneFeature.objects.all()
    return render_to_response('scenes_features/index.html',{'data':data})
    pass

def scene_feature(request,id):
    data =  SceneFeature.objects.filter(id=id)[0]
    return render_to_response('scenes_features/entry.html',{'data':data})
    pass
# Create your views here.
