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

class SingleView(View):
    def get(self,request):
        return render(request,'single.html')
