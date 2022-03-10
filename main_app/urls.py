from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('default/', views.Default.as_view(), name="default"),
    path('posts/', views.AllPost.as_view(), name="all_post"),
    path('posts/new/', views.CreatePost.as_view(), name="create_post")
]