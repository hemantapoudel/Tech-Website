from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'index.html')

class SingleView(View):
    def get(self,request):
        return render(request,'single.html')
