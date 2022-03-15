from poplib import POP3_SSL_PORT
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Post, Comment 
from django.shortcuts import redirect 
from django.urls import reverse

# imports related to feed
from django.contrib.syndication.views import Feed
from main_app.models import Post

# imports related to signup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# authorization decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class Home(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['posts'] = posts
        
        context['posts'] = Post.objects.order_by("-created_at")[:5]
        context['header'] = "Latest Post"
        return context


    


@method_decorator(login_required, name="dispatch")
class AllPost(TemplateView):
    template_name="all_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['posts'] = posts
        name = self.request.GET.get("title")
        print(name)
        if name != None:
            context['posts'] = Post.objects.filter(title__icontains=name, user=self.request.user)
            context['header'] = f"Results for: {name}"
        else:    
            context['posts'] = Post.objects.filter(user=self.request.user)
            context['header'] = "All Posts"
        return context

@method_decorator(login_required, name="dispatch")
class CreatePost(CreateView):
    model = Post
    fields = ['title', 'image', 'body_text']
    template_name = 'create_post.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})   


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
        Comment.objects.create(comment_text=comment_text, post=post, user=self.request.user)
        return redirect('post_detail', pk=pk)

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_post')
        else:
            context={"form": form}
            return render(request, "registration/signup.html", context)    




#  (phase 2 rss feature)
# class PostFeed(Feed):
#     title = "My posts"
#     link= ""
#     description_template= "all_post.html"

#     def items(self):
#         return Post.objects.order_by('created_at')[:5]

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['foo'] = 'bar'
#         return context

