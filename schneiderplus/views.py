from django.shortcuts import render
from blog.models import *
from .models import *
from brand.models import *
from category.models import *
from product.models import *

def fourzerofour(request):

    return render(request, 'schneiderplus/404.html')

def landing_page(request):
    status_slider = 404
    status_blog = 404
    status_specialblog = 404
    status_support = 404
    status_brand = 404
    status_category = 404
    status_newestproduct = 404
    status_hypeproduct = 404
    status_higheproduct = 404

    #Get support
    if Support.objects.filter().exists():
        status_support = 200
        support = Support.objects.get()

    # get sliders
    sliders = Slider.objects.none()
    if Slider.objects.filter(active=True).exists():
        status_slider = 200
        sliders = Slider.objects.filter(active=True).order_by('-id')


    # get blogs
    blogs = Blog.objects.none()
    if Blog.objects.filter(active=True, special_blog=False).exists():
        status_blog = 200
        blogs = Blog.objects.filter(active=True, special_blog=False).order_by('-J_editition_datetime')[:3]

    # get special blog 
    specialblog = Blog.objects.none()
    if Blog.objects.filter(active=True, special_blog=True).exists():
        status_specialblog = 200
        specialblog = Blog.objects.filter(active=True, special_blog=True).order_by('-J_editition_datetime')[:1]

    
    # get brands
    brands = Brand.objects.none()
    if Brand.objects.filter(active=True).exists():
        status_brand = 200
        brands = Brand.objects.filter(active=True)

    
    # get categories
    categories = ProductCategory.objects.none()
    if ProductCategory.objects.filter(active=True).exists():
        status_category = 200
        categories = ProductCategory.objects.filter(active=True)

    # get products

        # newest
    newest_products = Product.objects.none()
    if Product.objects.filter(active=True).exists():
        newest_products = Product.objects.filter(active=True).order_by('-id')[:10]
        status_newestproduct = 200

        # high veiw
    high_products = Product.objects.none()
    if Product.objects.filter(active=True).exists():
        high_products = Product.objects.filter(active=True).order_by('-view')[:10]
        status_higheproduct = 200

    
    context = {
        'status_support' : status_support,
        'support' : support,

        'status_slider' : status_slider,
        'sliders' : sliders,

        'status_blog' : status_blog,
        'blogs' : blogs,
        'status_specialblog' : status_specialblog,
        'specialblog' : specialblog,

        'status_brand' : status_brand,
        'brands' : brands,

        'status_category' : status_category,
        'categories' : categories,

        'status_newestproduct' : status_newestproduct,
        'newest_products' : newest_products,

        'status_higheproduct' : status_higheproduct,
        'high_products' : high_products,
    }

    return render(request, 'schneiderplus/landingpage.html', context)

def about_us(request):


    return render(request, 'schneiderplus/aboutus.html')

def contact_us(request):
    status = 404
    if Support.objects.filter().exists():
        status = 200
        support = Support.objects.get()

    if status == 404 :
        return redirect('/404')
    context = {
        'status':status,
        'support':support,
    }

    return render(request, 'schneiderplus/contactus.html', context)