
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('<str:url>/', views.categories, name="categories"),
    path('<str:reference>/<str:url>/', views.subset, name="subset"),
]
