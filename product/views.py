from django.shortcuts import render
from .models import *
from brand.models import *
from category.models import *
from schneiderplus.models import Support
from django.core.paginator import Paginator

def products(request):
    status = 404
    status_support = 404
    similar_products_status = 404


    #Get support
    if Support.objects.filter().exists():
        status_support = 200
        support = Support.objects.get()
    
    # get brand
    brand_object = Brand.objects.none()
    if Brand.objects.filter(active=True).exists():
        brand_object = Brand.objects.get(active=True)
        print(brand_object)

    # get product
    product_objects = Product.objects.none()
    if Product.objects.filter(active=True).exists():
        product_objects = Product.objects.filter(active=True)
        print(product_objects)

    # PAGINATION
        page_num  = request.GET.get('page',1)
        paginator = Paginator(product_objects, 16)

        try:
            products = paginator.page(page_num)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            products = paginator.page(1)
        except EmptyPage:
            # if page is empty then return last page
            products = paginator.page(paginator.num_pages)

        #...HowManyObjectAreInThisList
        # NumberOfProducts = ObjectsCounter(product_objects)
        # NumberOfProductsIn1Page = NumberOfProducts // int(paginator.num_pages)
    # PAGINATION

    # get category
    # category_object = ProductCategory.objects.none()
    # subset_object = ProductCategorySubset.objects.none()
    # if ProductCategory.objects.filter(active=True).exists():
    #     category_object = ProductCategory.objects.get(active=True)
    #     print(category_object)

    #     # get subset
    #     if ProductCategorySubset.objects.filter(active=True).exists():
    #         subset_object = ProductCategorySubset.objects.get(active=True)
    #         print(subset_object)




    
    context = {
        'status_support':status_support,
        'support':support,
        'products':products,
        # 'categories':category_object,
        # 'subsets':subset_object,
    }

    return render(request, 'schneiderplus/product/products.html', context)


def product_details(request, brand, category, subset, enName):
    status = 404
    status_support = 404
    similar_products_status = 404


    #Get support
    if Support.objects.filter().exists():
        status_support = 200
        support = Support.objects.get()
    
    # get brand
    brand_object = Brand.objects.none()
    if Brand.objects.filter(active=True, en_name=brand).exists():
        brand_object = Brand.objects.get(active=True, en_name=brand)
        print(brand_object)

    # get product
    product_object = Product.objects.none()
    if Product.objects.filter(active=True, enName=enName).exists():
        product_object = Product.objects.get(active=True, enName=enName)
        print(product_object)

        taglist = product_object.tags.split(',')


        # get productimages
        productimages_object = ProductImage.objects.none()
        if ProductImage.objects.filter(active=True, Product=product_object).exists():
            productimages_object = ProductImage.objects.filter(active=True, Product=product_object)

        # get features
        features_object = Feature.objects.none()
        if Feature.objects.filter(active=True, Product=product_object).exists():
            features_object = Feature.objects.filter(active=True, Product=product_object)

        featurescats_objects = FeaturesCategories.objects.none()
        if FeaturesCategories.objects.filter(active=True).exists():
            featurescats_objects = FeaturesCategories.objects.filter(active=True)


    # get category
    category_object = ProductCategory.objects.none()
    subset_object = ProductCategorySubset.objects.none()
    similar_products = Product.objects.none()
    if ProductCategory.objects.filter(active=True, url=category).exists():
        category_object = ProductCategory.objects.get(active=True, url=category)
        print(category_object)

        # get subset
        if ProductCategorySubset.objects.filter(active=True, url=subset).exists():
            subset_object = ProductCategorySubset.objects.get(active=True, url=subset)
            print(subset_object)

            
            if Product.objects.filter(active=True, ProductCategorySubset=subset_object).exclude(active=True, enName=enName).exists():
                similar_products = Product.objects.filter(active=True, ProductCategorySubset=subset_object).exclude(active=True, enName=enName)[:10]
                similar_products_status = 200


    
    context = {
        'status_support':status_support,
        'support':support,
        'product':product_object,
        'taglist':taglist,
        'productimages':productimages_object,
        'features':features_object,
        'featurescats':featurescats_objects,
        'similar_products':similar_products,
        'similar_products_status':similar_products_status,
    }

    return render(request, 'schneiderplus/product/product_details.html', context)