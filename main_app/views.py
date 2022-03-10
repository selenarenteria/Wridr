from poplib import POP3_SSL_PORT
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView 
from django.http import HttpResponse
from .models import Post 

# STATIC DATA
# Class
# class Post:
#     def __init__(self, title, image, body_text):
#          self.title=title
#          self.image=image
#          self.body_text=body_text


# Seed data 
# posts = [
#     Post("SUGA day!", "https://i.imgur.com/eFmSPh9.jpeg", "Today is SUGA also known as Min Yoongi from BTS's birthday!!!"),
#     Post("SOPE appreciation post", "https://i.imgur.com/KQIPsCJs.jpeg", "SOPE is the best duo in BTS!")
# ]
# Create your views here.

class Home(TemplateView):
    template_name="home.html"
    # def get(self, request):
    #     return HttpResponse("Selena Welcome Home!")
    


class Default(TemplateView):
    template_name="default.html"
    # def get(self, request):
    #     return HttpResponse("This is the default page")


class AllPost(TemplateView):
    template_name="all_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['posts'] = posts
        title = self.request.GET.get("title")
        print(title)
        if title != None:
            context['posts'] = Post.objects.filter(title__icontains=title)
        else:    
            context['posts'] = Post.objects.all()
        return context

