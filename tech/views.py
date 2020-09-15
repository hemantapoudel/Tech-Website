from django.shortcuts import render
from django.views.generic.base import View
from .models import *

# Create your views here.
class BaseView(View):
    frontend_view={}

class HomeView(BaseView):
    def get(self,request):
        self.frontend_view['posts']=Posts.objects.all()
        return render(request,'index.html',self.frontend_view)

class SingleView(BaseView):
    def get(self,request,slug):
        
        self.frontend_view['view_post']=Posts.objects.filter(slug=slug)
        return render(request,'single.html')
