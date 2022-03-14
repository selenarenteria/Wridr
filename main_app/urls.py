from unicodedata import name
from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('posts/', views.AllPost.as_view(), name="all_post"),
    path('posts/new/', views.CreatePost.as_view(), name="create_post"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update', views.UpdatePost.as_view(), name="update_post"),
    path('posts/<int:pk>/delete', views.DeletePost.as_view(), name="delete_post"),
    path('posts/<int:pk>/comments/new', views.LeaveComment.as_view(), name="leave_comment"),
    path('accounts/signup', views.Signup.as_view(), name="signup")
]