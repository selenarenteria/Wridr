from poplib import POP3_SSL_PORT
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Post, Comment 
from django.shortcuts import redirect 

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
        name = self.request.GET.get("title")
        print(name)
        if name != None:
            context['posts'] = Post.objects.filter(title__icontains=name)
            context['header'] = f"Results for: {name}"
        else:    
            context['posts'] = Post.objects.all()
            context['header'] = "All Posts"
        return context

class CreatePost(CreateView):
    model = Post
    fields = ['title', 'image', 'body_text']
    template_name = 'create_post.html'
    success_url = '/posts/'


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

class UpdatePost(UpdateView):
    model = Post
    fields = ['title', 'image', 'body_text']
    template_name = 'update_post.html'
    success_url = '/posts/'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post_confirmation.html'
    success_url = '/posts/'

class LeaveComment(View):
    def post(self, request, pk):
        comment_text = request.POST.get("comment_text")
        post = Post.objects.get(pk=pk)
        Comment.objects.create(comment_text=comment_text, post=post)
        return redirect('post_detail', pk=pk)





