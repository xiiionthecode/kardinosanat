from django.shortcuts import render
from .models import *
from brand.models import *
from schneiderplus.models import *
from product.models import *

def categories(request, url):
    status_support = 404
    status_brand = 404
    status_category = 404
    status_product = 404
    status_subset = 404

    #Get support
    if Support.objects.filter().exists():
        status_support = 200
        support = Support.objects.get()

    
    # get brands
    brands = Brand.objects.none()
    if Brand.objects.filter(active=True).exists():
        status_brand = 200
        brands = Brand.objects.filter(active=True)

    
    # get category
    category = ProductCategory.objects.none()
    allproducts = Product.objects.none()
    products = []
    counter = 0
    if ProductCategory.objects.filter(active=True, url=url).exists():
        status_category = 200
        category = ProductCategory.objects.get(active=True, url=url)

        # get products
        if Product.objects.filter(active=True).exists():
            status_product = 200
            allproducts = Product.objects.filter(active=True)

            for product in allproducts:
                if product.ProductCategorySubset.ProductCategory == category and counter <= 10:
                    counter += 1
                    products.append(product)

            

    
    # get subsets
    subsets = ProductCategorySubset.objects.none()
    if ProductCategorySubset.objects.filter(active=True, ProductCategory=category, subset_number=2).exists():
        status_category = 200
        subsets = ProductCategorySubset.objects.filter(active=True, ProductCategory=category, subset_number=2).order_by('position')

    
    context = {
        'status_support' : status_support,
        'support' : support,

        'status_brand' : status_brand,
        'brands' : brands,

        'status_category' : status_category,
        'category' : category,

        'status_product' : status_product,
        'products' : products,

        'status_subset' : status_subset,
        'subsets' : subsets,
    }

    return render(request, 'schneiderplus/category/category.html', context)


def subset(request, reference, url):
    status_product = 404
    status_support = 404
    status_brand = 404
    status_category = 404
    status_subset = 404

    print(reference)
    print('reference')
    print(url)
    print('url')

    subset_objects = ProductCategorySubset.objects.none()
    ref = ProductCategorySubset.objects.none()



    
    #Get support
    if Support.objects.filter().exists():
        status_support = 200
        support = Support.objects.get()

    
    # get brands
    brands = Brand.objects.none()
    if Brand.objects.filter(active=True).exists():
        status_brand = 200
        brands = Brand.objects.filter(active=True)

    if ProductCategorySubset.objects.filter(active=True, url=url).exists():
        ref = ProductCategorySubset.objects.get(active=True, url=url)
        if ProductCategorySubset.objects.filter(active=True, ref_slug=ref.slug).exists():
            subset_objects = ProductCategorySubset.objects.filter(active=True, ref_slug=ref.slug)

            # get category
            category = ProductCategory.objects.none()
            allproducts = Product.objects.none()
            products = []
            counter = 0
            if ProductCategory.objects.filter(active=True, url=reference).exists():
                status_category = 200
                category = ProductCategory.objects.get(active=True, url=reference)

                # get products
                if Product.objects.filter(active=True).exists():
                    status_product = 200
                    allproducts = Product.objects.filter(active=True)

                    for product in allproducts:
                        if product.ProductCategorySubset.ProductCategory == category and counter <= 10:
                            counter += 1
                            products.append(product)
    print(ref)
    print('ref')
    context = {

        'status_support' : status_support,
        'support' : support,

        'status_brand' : status_brand,
        'brands' : brands,

        'status_product' : status_product,
        'products' : products,

        'status_subset' : status_subset,
        'subsets' : subset_objects,
        'ref' : ref,
    }

    return render(request, 'schneiderplus/category/subset.html', context)

