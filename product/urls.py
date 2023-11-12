from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.products, name="allproducts"),
    path('<str:brand>/<str:category>/<str:subset>/<str:enName>/', views.product_details, name="products"),
]