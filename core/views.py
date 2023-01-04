from django.shortcuts import render
from django.views import View #function that takes a web request and return a web response

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'index.html')

