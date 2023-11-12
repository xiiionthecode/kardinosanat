from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('<str:url>/', views.blog_details, name="blog_det"),

    
    # re_path(r's/(?P<search_word>[-\w\s]+)/', views.search, name="bSearch"),

]