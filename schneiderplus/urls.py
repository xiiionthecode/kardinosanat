
from django.urls import path, include, re_path
from schneiderplus import views

urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path('404', views.fourzerofour, name="404"),
    path('about_us/', views.about_us, name="about_us"),
    path('contact_us/', views.contact_us, name="contact_us"),
]
