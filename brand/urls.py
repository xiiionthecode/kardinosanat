
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('<str:url>/', views.blog_details, name="brand_det"),
]
