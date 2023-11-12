from django.shortcuts import render, redirect
from .models import *
from brand.models import Brand


def blogs(request):
    status = 404
    status_brand = 404

    blogs = Blog.objects.none()

    #get this page blog
    if Blog.objects.filter(active=True).exists():
        status = 200
        blogs = Blog.objects.filter(active=True)

    # get brands
    brands = Brand.objects.none()
    if Brand.objects.filter(active=True).exists():
        status_brand = 200
        brands = Brand.objects.filter(active=True)

    if status == 404 :
        return redirect('/404')

    context ={
        'status' : status,
        'blogs' : blogs,

        'status_brand' : status_brand,
        'brands' : brands,
    }

    return render(request, 'schneiderplus/blog/blogs.html', context)

def blog_details(request, url):
    status = 404
    status_brand = 404

    blog = Blog.objects.none()

    #get this page blog
    if Blog.objects.filter(active=True, url=url).exists():
        status = 200
        blog = Blog.objects.get(active=True, url=url)

        blog_tags = (blog.tags).split(',')

        blog.view = blog.view + 1
        blog.save()

        #get top5 popular blogs
        popular_blogs = Blog.objects.filter(active=True).exclude(url=url).order_by('-view')[:4]

    # get brands
    brands = Brand.objects.none()
    if Brand.objects.filter(active=True).exists():
        status_brand = 200
        brands = Brand.objects.filter(active=True)
    
    if status == 404 :
        return redirect('/404')

    context ={
        'status' : status,
        'blog' : blog,
        'blog_tags' : blog_tags,
        'popular_blogs' : popular_blogs,

        'status_brand' : status_brand,
        'brands' : brands,
    }

    return render(request, 'schneiderplus/blog/blog_details.html', context)


# def search(request, search_word):
#     status = 404
#     search_status = 500

#     blogs = Blog.objects.none()
#         #get this page blog
#         if Blog.objects.filter(active=True).exists():
#             status = 200
#             blogs = Blog.objects.filter(active=True)

#             if search_word != '':
#                 for blog in blogs:
#                     title = blog.title
#                     description = blog.description
#                     description = blog.description

#                     if search(searchboxvalue.lower(), enName.lower()):
#                         # thisValue = {'faName':faName.lower(), 'code':code,  'url':'/Products/'+ product.Brand.url + '/' + product.ProductType.ProductCategory.url + '/' + product.ProductType.url + '/' + product.url, 'typeresault':'از محصولات'}
#                         thisValue = {'faName':faName.lower(), 'code':code,  'url':'/Products/'+ product.Brand.url + '/' + product.ProductType.ProductCategory.url + '/' + product.ProductType.url + '/' + product.url, 'typeresault':'از محصولات'}
#                         if thisValue not in searchresault:
#                             searchresault.append({'faName':faName.lower(), 'code':code,  'url':'/Products/'+ product.Brand.url + '/' + product.ProductType.ProductCategory.url + '/' + product.ProductType.url + '/' + product.url, 'typeresault':'از محصولات'})
#                             status = 200
                
        


#     if status == 404 :
#         return redirect('/404')

#     context ={
#         'status' : status,
#         'blogs' : blogs,
#     }

#     return render(request, 'schneiderplus/blog/search.html', context)
