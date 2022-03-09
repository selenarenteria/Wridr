from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView 
from django.http import HttpResponse

# Create your views here.

class Home(TemplateView):
    template_name="home.html"
    # def get(self, request):
    #     return HttpResponse("Selena Welcome Home!")
    


class Default(TemplateView):
    template_name="default.html"
    # def get(self, request):
    #     return HttpResponse("This is the default page")


# class All
