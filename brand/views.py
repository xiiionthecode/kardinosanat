from django.shortcuts import render, redirect
from .models import *

def blog_details(request, url):
    status = 404
    status_brand = 404
    status_products = 404
    

    brand = Brand.objects.none()

    #get this page blog
    if Brand.objects.filter(active=True, url=url).exists():
        status = 200
        brand = Brand.objects.get(active=True, url=url)


        #get top5 popular blogs
        # popular_blogs = Blog.objects.filter(active=True).exclude(url=url).order_by('-view')[:4]
    
    # get brands
    brands = Brand.objects.none()
    if Brand.objects.filter(active=True).exists():
        status_brand = 200
        brands = Brand.objects.filter(active=True)
    
    if status == 404 :
        return redirect('/404')

    context ={
        'status' : status,
        'brand' : brand,

        'status_products' : status_products,

        'status_brand' : status_brand,
        'brands' : brands,
    }

    return render(request, 'schneiderplus/brand/brand_details.html', context)