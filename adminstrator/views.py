from django.shortcuts import render, redirect
from datetime import date
from django.db.models import Q
from logs.models import *
import uuid, os, jdatetime
from .models import AdminLogin, AdminInfo
from blog.models import *
from blog.forms import *
from schneiderplus.defplus import CMNtL
from schneiderplus.models import *
from brand.forms import *
from brand.models import *
from category.models import *
from category.forms import *
from product.models import *
from product.forms import *

def login(request):

    return render(request, 'adminstrator/login.html')

def dashboard(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        title = 'Dashboard'
        tagid = 'dashboard'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)
        
        context = {
            'title':title,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
        }

    return render(request, 'adminstrator/dashboard/dashboard.html', context)



def manage_blogs(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'Dashboard'
        tagid = 'blogs'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        blog_objects = Blog.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)
        
                if Blog.objects.filter(active=True).exists():
                    blog_objects = Blog.objects.filter(active=True)
                

        context = {
            'PageTitle':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'blogs' :blog_objects,
        }

    return render(request, 'adminstrator/dashboard/blog/manage_blogs.html', context)

def add_blog(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'اضافه کردن بلاگ'
        tagid = 'blogs'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)

                #add blog_form to variable for send to front
                form = blog_form()

                #start save form data
                if request.POST :
                    if 'addblogBTN' in request.POST:
                        url = request.POST.get('url', 'null')
                        title = request.POST.get('title', 'null')
                        tags = request.POST.get('tags', 'null')
                        description = request.POST.get('description', 'null')
                        poster = request.FILES.get('poster', 'null')
                        second_poster = request.FILES.get('second_poster', 'null')
                        articleText = request.POST.get('article_text', 'null')
                        checkbox = request.POST.get('specialcheckbox', 'null')

                        #Preparation checkbox value for save to boolean
                        if checkbox == 'on':
                            checkbox = True
                        else :
                            checkbox = False

                        date = str(jdatetime.date.today())
                        datesplited = date.split('-')

                        #create new Blog object for saving data
                        blogObject = Blog.objects.create(
                            author = login_object,
                            author_info = info_object,
                            url = url,
                            title = title,
                            tags = tags,
                            description = description,
                            poster = poster,
                            second_poster = second_poster,
                            article_text = articleText,
                            special_blog = checkbox,
                            J_addition_datetime = jdatetime.date.today(),
                            J_editition_datetime = jdatetime.date.today(),
                            day = str(datesplited[2]),
                            month = str(CMNtL(datesplited[1])),
                            year = str(datesplited[0]),
                            )

                        #create new Tag object for saving data
                        taglist = tags.split(',')
                        for tag in taglist :
                            #if this tags are exists just add one unit to number of used 
                            if BlogTag.objects.filter(active=True, name=tag).exists():
                                blogtagObject = BlogTag.objects.get(active=True, name=tag)
                                numberOfUsed = blogtagObject.numberOfUsed
                                blogtagObject.numberOfUsed = numberOfUsed + 1
                                blogtagObject.save()
                            #create new Tag object if this tag is new
                            else:
                                BlogTag.objects.create(
                                    name = tag
                                )

        context = {
            'title':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'form':form,
        }

    return render(request, 'adminstrator/dashboard/blog/add_blog.html', context)

def edit_blog(request, slug):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'Dashboard'
        tagid = 'blogs'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        blog_objects = Blog.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)

                if Blog.objects.filter(active=True, slug=slug).exists():
                    blog_object = Blog.objects.get(active=True, slug=slug)

                    # send form to front end
                    form = blog_form(instance = blog_object)

                    # start save form data
                    if request.POST :
                        if 'editblogBTN' in request.POST:
                            url = request.POST.get('url', 'null')
                            title = request.POST.get('title', 'null')
                            tags = request.POST.get('tags', 'null')
                            description = request.POST.get('description', 'null')
                            poster = request.FILES.get('poster', 'null')
                            second_poster = request.FILES.get('second_poster', 'null')
                            article_text = request.POST.get('article_text', 'null')
                            checkbox = request.POST.get('specialcheckbox', 'null')



                            taglist = tags.split(',')
                            # Low-off tags number of used
                            for tag in taglist:
                                if BlogTag.objects.filter(active=True, name=tag).exists():
                                    blogtagObject = BlogTag.objects.get(active=True, name=tag)
                                    numberOfUsed = blogtagObject.numberOfUsed
                                    if numberOfUsed - 1 != 0 :
                                        blogtagObject.numberOfUsed = numberOfUsed - 1
                                        blogtagObject.save()
                                    if numberOfUsed - 1 == 0:
                                        blogtagObject.active = False
                                        blogtagObject.save()

                            # create new Tag object for saving data
                            for tag in taglist :
                                #if this tags are exists just add one unit to number of used 
                                if BlogTag.objects.filter(active=True, name=tag).exists():
                                    blogtagObject = BlogTag.objects.get(active=True, name=tag)
                                    numberOfUsed = blogtagObject.numberOfUsed
                                    blogtagObject.numberOfUsed = numberOfUsed + 1
                                    blogtagObject.save()
                                #create new Tag object if this tag is new
                                else:
                                    BlogTag.objects.create(
                                        name = tag
                                    )

                            
                            # Preparation checkbox value for save to boolean
                            if checkbox == 'on':
                                checkbox = True
                            else :
                                checkbox = False

                            date = str(jdatetime.date.today())
                            datesplited = date.split('-')
                            print(datesplited[2])

                            # update Blog object for saving new data
                            blog_object.url = url
                            blog_object.title = title
                            blog_object.tags = tags
                            blog_object.description = description
                            if poster != 'null':
                                blog_object.poster = poster
                            if poster != 'null':
                                blog_object.second_poster = second_poster
                            blog_object.article_text = article_text
                            blog_object.special_blog = checkbox
                            blog_object.J_editition_datetime = jdatetime.date.today()
                            
                            blog_object.save()
                            Blog.objects.filter(active=True, url=url).update(
                                day=datesplited[2],
                                month=CMNtL(datesplited[1]),
                                year=datesplited[0]
                            )

                            print(blog_object.day)
                            print(blog_object.month)
                            print(blog_object.year)
                

        context = {
            'PageTitle':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'blog_object':blog_object,
            'form':form,
        }

    return render(request, 'adminstrator/dashboard/blog/edit_blog.html', context)

def deActive_blog(request, slug):
    status = 500
    msg=''

    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        blog = Blog.objects.none()
        admin_username = request.session['admin_login_username']
        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if Blog.objects.filter(active=True, slug=slug).exists():
                blog = Blog.objects.filter(active=True, slug=slug) 
                BlogLogs.objects.create(
                    author = login_object,
                    status = 'This blog has been deactive',
                    J_addition_datetime = jdatetime.date.today()
                )
                Blog.objects.filter(active=True, slug=slug).update(active=False)
                status = 200
                msg = 'بلاگ مورد نظر با موفقیت غیرفعال شد .'

        

    context = {
        'status':status,
        'msg':msg,
    }
    
    return redirect('/v1/adminstrator/dashboard/manage_blogs/')
    


def manage_brands(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'Dashboard'
        tagid = 'brands'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        brand_object = Brand.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)
        
                if Brand.objects.filter(active=True).exists():
                    brand_object = Brand.objects.all()
                

        context = {
            'PageTitle':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'brands' :brand_object,
        }

    return render(request, 'adminstrator/dashboard/brand/manage_brands.html', context)

def add_brand(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'اضافه کردن برند'
        tagid = 'brands'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)

                #add brand_form to variable for send to front
                form = brand_form()

        #         #start save form data
                if request.POST :
                    if 'addbrandBTN' in request.POST:
                        url = request.POST.get('url', 'null')
                        fa_name = request.POST.get('fa_name', 'null')
                        en_name = request.POST.get('en_name', 'null')
                        country = request.POST.get('country', 'null')
                        founded_date = request.POST.get('founded_date', 'null')
                        number_of_employees = request.POST.get('number_of_employees', 'null')
                        brief_explamations = request.POST.get('brief_explamations', 'null')
                        descriptions = request.POST.get('descriptions', 'null')
                        logo_1th = request.FILES.get('logo_1th', 'null')
                        logo_2th = request.FILES.get('logo_2th', 'null')
                        logo_blured = request.FILES.get('logo_blured', 'null')
                        logo_slider = request.FILES.get('logo_slider', 'null')

                        #create new Blog object for saving data
                        brandObject = Brand.objects.create(
                            url = url,
                            fa_name = fa_name,
                            en_name = en_name,
                            country = country,
                            founded_date = founded_date,
                            number_of_employees = number_of_employees,
                            brief_explamations = brief_explamations,
                            descriptions = descriptions,
                            logo_1th = logo_1th,
                            logo_2th = logo_2th,
                            logo_blured = logo_blured,
                            logo_slider = logo_slider,
                            )

        context = {
            'title':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'form':form,
        }

    return render(request, 'adminstrator/dashboard/brand/add_brand.html', context)

def edit_brand(request, id):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'Dashboard'
        tagid = 'brands'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        brand_object = Brand.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)

                if Brand.objects.filter(active=True, id=id).exists():
                    brand_object = Brand.objects.get(active=True, id=id)

                    # send form to front end
                    form = brand_form(instance = brand_object)

        #             # start save form data
                    if request.POST :
                        if 'editbrandBTN' in request.POST:
                            fa_name = request.POST.get('fa_name', 'null')
                            en_name = request.POST.get('en_name', 'null')
                            brief_explamations = request.POST.get('brief_explamations', 'null')
                            descriptions = request.POST.get('descriptions', 'null')
                            country = request.POST.get('country', 'null')
                            logo_1th = request.FILES.get('logo_1th', 'null')
                            logo_2th = request.FILES.get('logo_2th', 'null')
                            logo_blured = request.FILES.get('logo_blured', 'null')
                            logo_slider = request.FILES.get('logo_slider', 'null')
                            number_of_employees = request.POST.get('number_of_employees', 'null')
                            founded_date = request.POST.get('founded_date', 'null')
                            url = request.POST.get('url', 'null')
                                                       
                            # update Brand object for saving new data
                            brand_object.url = url
                            brand_object.fa_name = fa_name
                            brand_object.en_name = en_name
                            brand_object.brief_explamations = brief_explamations
                            brand_object.descriptions = descriptions
                            brand_object.country = country
                            if logo_1th != 'null':
                                brand_object.logo_1th = logo_1th
                            if logo_2th != 'null':
                                brand_object.logo_2th = logo_2th
                            if logo_blured != 'null':
                                brand_object.logo_blured = logo_blured
                            if logo_slider != 'null':
                                brand_object.logo_slider = logo_slider
                            brand_object.number_of_employees = number_of_employees
                            brand_object.founded_date = founded_date
                            brand_object.save()

        context = {
            'PageTitle':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'brand_object':brand_object,
            'form':form,
        }

    return render(request, 'adminstrator/dashboard/brand/edit_brand.html', context)

def deActive_brand(request, id):
    status = 500
    msg=''

    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        brand = Brand.objects.none()
        admin_username = request.session['admin_login_username']
        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if Brand.objects.filter(active=True, id=id).exists():
                brand = Brand.objects.filter(active=True, id=id) 
                BrandLogs.objects.create(
                    author = login_object,
                    status = 'This brand has been deactive',
                    J_addition_datetime = jdatetime.date.today()
                )
                Brand.objects.filter(active=True, id=id).update(active=False)
                status = 200
                msg = 'برند مورد نظر با موفقیت غیرفعال شد .'

        

    context = {
        'status':status,
        'msg':msg,
    }
    
    return redirect('/v1/adminstrator/dashboard/manage_brands/')



def manage_pcategory(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'Dashboard'
        tagid = 'catandtype'
        submenu = 'true'
        active = 'cats'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        category_objects = ProductCategory.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)
        
                if ProductCategory.objects.filter(active=True).exists():
                    category_objects = ProductCategory.objects.all()
                

        context = {
            'PageTitle':PageTitle,
            'tagid':tagid,
            'submenu':submenu,
            'active':active,
            'admin_login':login_object,
            'admin_info':info_object,
            'categories' :category_objects,
        }

    return render(request, 'adminstrator/dashboard/category/manage-categories.html', context)

def add_pcategory(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'Dashboard'
        tagid = 'catandtype'
        submenu = 'true'
        active = 'cats'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)

                #add ProductCategory_form to variable for send to front
                form = ProductCategory_form()

                #start save form data
                if request.POST :
                    if 'addcatBTN' in request.POST:
                        url = request.POST.get('url', 'null')
                        name = request.POST.get('name', 'null')
                        vector = request.FILES.get('vector', 'null')
                        position = request.POST.get('position', 'null')
                        number_of_products = 0
                        print(position)
                        print('position')

                        #create new ProductCategory object for saving data
                        category_object = ProductCategory.objects.create(
                            url = url,
                            name = name,
                            vector = vector,
                            position = position,
                            number_of_products = number_of_products,
                            )

        context = {
            'title':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'form':form,
        }

    return render(request, 'adminstrator/dashboard/category/add_category.html', context)

def edit_pcategory(request, slug):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'Dashboard'
        tagid = 'catandtype'
        submenu = 'true'
        active = 'cats'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        category_object = ProductCategory.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)

                if ProductCategory.objects.filter(active=True, slug=slug).exists():
                    category_object = ProductCategory.objects.get(active=True, slug=slug)

                    # send form to front end
                    form = ProductCategory_form(instance = category_object)

        #             # start save form data
                    if request.POST :
                        if 'editcatBTN' in request.POST:
                            url = request.POST.get('url', 'null')
                            name = request.POST.get('name', 'null')
                            vector = request.FILES.get('vector', 'null')
                            position = request.POST.get('position', 'null')
                                                       
                            # update Brand object for saving new data
                            category_object.url = url
                            category_object.name = name
                            category_object.position = position
                            if vector != 'null':
                                category_object.vector = vector
                            category_object.save()

        context = {
            'PageTitle':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'category_object':category_object,
            'form':form,
        }

    return render(request, 'adminstrator/dashboard/category/edit_category.html', context)

def deActive_pcategory(request, slug):
    status = 500
    msg=''

    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        category = ProductCategory.objects.none()
        admin_username = request.session['admin_login_username']
        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if ProductCategory.objects.filter(active=True, slug=slug).exists():
                category = ProductCategory.objects.filter(active=True, slug=slug) 
                Categorylogs.objects.create(
                    author = login_object,
                    status = 'This category has been deactive',
                    J_addition_datetime = jdatetime.date.today()
                )
                ProductCategory.objects.filter(active=True, slug=slug).update(active=False)
                status = 200
                msg = 'دسته بندی مورد نظر با موفقیت غیرفعال شد .'

        

    context = {
        'status':status,
        'msg':msg,
    }
    
    return redirect('/v1/adminstrator/dashboard/manage_pcategories/')



def manage_psubset(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'Dashboard'
        tagid = 'catandtype'
        submenu = 'true'
        active = 'types'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        subset_objects = ProductCategorySubset.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)
        
                if ProductCategorySubset.objects.filter(active=True).exists():
                    subset_objects = ProductCategorySubset.objects.filter(active=True)
                

        context = {
            'PageTitle':PageTitle,
            'tagid':tagid,
            'submenu':submenu,
            'active':active,
            'admin_login':login_object,
            'admin_info':info_object,
            'subsets' :subset_objects,
        }

    return render(request, 'adminstrator/dashboard/category/manage_subset.html', context)

def add_psubset(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'Dashboard'
        tagid = 'catandtype'
        submenu = 'true'
        active = 'types'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        category_objects = ProductCategory.objects.none()
        subset_objects = ProductCategorySubset.objects.none()
        ref = []

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)

                # Get all Categories
                if ProductCategory.objects.filter(active=True).exists():
                    category_objects = ProductCategory.objects.filter(active=True)

                # Get all Subsets
                if ProductCategorySubset.objects.filter(active=True).exists():
                    subset_objects = ProductCategorySubset.objects.filter(active=True)

                #add ProductCategorySubset_form to variable for send to front
                form = ProductCategorySubset_form()

                #start save form data
                if request.POST :
                    if 'addcatBTN' in request.POST:
                        url = request.POST.get('url', 'null')
                        name = request.POST.get('name', 'null')
                        vector = request.FILES.get('vector', 'null')
                        ref_slug = request.POST.get('ProductCategory', 'null')
                        subset_number = request.POST.get('subset_number', 'null')
                        position = request.POST.get('position', 'null')
                        number_of_products = 0
                        print(subset_number)
                        print('subset_number')

                        # Get this subset ProductCategory
                        if ProductCategory.objects.filter(slug=ref_slug, active=True).exists():
                            ref = ProductCategory.objects.get(slug=ref_slug, active=True)

                            subset_object = ProductCategorySubset.objects.create(
                            url = url,
                            name = name,
                            vector = vector,
                            ref_slug = ref.slug,
                            ProductCategory = ref,
                            subset_number = subset_number,
                            position = position,
                            number_of_products = number_of_products,
                            )

                        # Get this subset ProductCategorySubset
                        if ProductCategorySubset.objects.filter(slug=ref_slug, active=True).exists():
                            ref = ProductCategorySubset.objects.get(slug=ref_slug, active=True)

                            subset_object = ProductCategorySubset.objects.create(
                            url = url,
                            name = name,
                            vector = vector,
                            ref_slug = ref.slug,
                            subset_number = subset_number,
                            position = position,
                            number_of_products = number_of_products,
                            )

                        #create new ProductCategorySubset object for saving data
                        

        context = {
            'title':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'categories':category_objects,
            'subsets':subset_objects,
            'form':form,
        }

    return render(request, 'adminstrator/dashboard/category/add_subset.html', context)

def edit_psubset(request, slug):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'Dashboard'
        tagid = 'catandtype'
        submenu = 'true'
        active = 'types'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        subset_object = ProductCategory.objects.none()
        category_object = ProductCategory.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)

                if ProductCategorySubset.objects.filter(active=True, slug=slug).exists():
                    subset_object = ProductCategorySubset.objects.get(active=True, slug=slug)

                    # Get this subset ProductCategory
                    if ProductCategory.objects.filter(active=True).exists():
                        category_object = ProductCategory.objects.filter(active=True)

                    # send form to front end
                    form = ProductCategorySubset_form(instance = subset_object)

                    # start save form data
                    if request.POST :
                        if 'editsubsetBTN' in request.POST:
                            url = request.POST.get('url', 'null')
                            name = request.POST.get('name', 'null')
                            vector = request.FILES.get('vector', 'null')
                            subset_number = request.POST.get('subset_number', 'null')
                            position = request.POST.get('position', 'null')
                                                       
                            # update ProductCategorySubset object for saving new data
                            subset_object.url = url
                            subset_object.name = name
                            subset_object.subset_number = subset_number
                            subset_object.position = position
                            if vector != 'null':
                                subset_object.vector = vector
                            subset_object.save()

        context = {
            'PageTitle':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'categories':category_object,
            'subset_object':subset_object,
            'form':form,
        }

    return render(request, 'adminstrator/dashboard/category/edit_subset.html', context)

def deActive_psubset(request, slug):
    status = 500
    msg=''

    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        subset = ProductCategorySubset.objects.none()
        admin_username = request.session['admin_login_username']
        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if ProductCategorySubset.objects.filter(active=True, slug=slug).exists():
                subset = ProductCategorySubset.objects.filter(active=True, slug=slug) 
                Subsetlogs.objects.create(
                    author = login_object,
                    status = 'This subset has been deactive',
                    J_addition_datetime = jdatetime.date.today()
                )
                ProductCategorySubset.objects.filter(active=True, slug=slug).update(active=False)
                status = 200
                msg = 'زیرمجموعه دسته بندی مورد نظر با موفقیت غیرفعال شد .'

        

    context = {
        'status':status,
        'msg':msg,
    }
    
    return redirect('/v1/adminstrator/dashboard/manage_psubsets/')


def manage_products(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'Dashboard'
        tagid = 'products'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        products_objects = Product.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)
        
                if Product.objects.filter(active=True).exists():
                    products_objects = Product.objects.filter(active=True)
                

        context = {
            'PageTitle':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'products' :products_objects,
        }

    return render(request, 'adminstrator/dashboard/product/manage_products.html', context)


def add_featurecats(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'اضافه کردن محصول'
        tagid = 'products'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        FeaturesCategories_objects = FeaturesCategories.objects.none()

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)

                if request.POST :
                    if 'addfeaturecatBTN' in request.POST:
                        feature = request.POST.get('feature', 'null')

                        FeaturesCategories.objects.create(
                            name = feature
                        )                

            context = {
                'title':PageTitle,
                'tagid':tagid,
                'admin_login':login_object,
                'admin_info':info_object,
            }

    return render(request, 'adminstrator/dashboard/product/add_featureCats.html', context)


def add_product(request):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'اضافه کردن محصول'
        tagid = 'products'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        brands_objects = Brand.objects.none()
        brand = Brand.objects.none()
        catsubsets_object = ProductCategorySubset.objects.none()
        catsubset = ProductCategorySubset.objects.none()
        product_object = Product.objects.none()
        productimage_object = ProductImage.objects.none()
        featurecat_object = FeaturesCategories.objects.none()
        feature_object = Feature.objects.none()
        producttagObject = ProductTag.objects.none()
        FeaturesCategories_objects = FeaturesCategories.objects.none()
        FeaturesCategories_status = 500



        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)

                #add product_form to variable for send to front
                product_form = Product_form()
                productImage_form = ProductImage_form()

                if Brand.objects.filter(active=True).exists():
                    brands_objects = Brand.objects.filter(active=True)
                
                if ProductCategorySubset.objects.filter(active=True).exists():
                    catsubsets_object = ProductCategorySubset.objects.filter(active=True)
                
                if FeaturesCategories.objects.filter(active=True).exists():
                    FeaturesCategories_objects = FeaturesCategories.objects.filter(active=True)
                    print(FeaturesCategories_objects)
                    FeaturesCategories_status = 200
                else:
                    FeaturesCategories_status = 404


                # #start save form data
                if request.POST :
                    if 'addproductBTN' in request.POST:

                        brand = request.POST.get('brand', 'null')
                        Subset = request.POST.get('Subset', 'null')
                        code = request.POST.get('code', 'null')
                        fa_name = request.POST.get('fa_name', 'null')
                        en_name = request.POST.get('en_name', 'null')
                        url = request.POST.get('url', 'null')
                        tags = request.POST.get('tags', 'null')
                        review = request.POST.get('review', 'null')
                        poster = request.FILES.get('poster', 'null')
                        

                        brand = Brand.objects.get(active=True, en_name=brand)
                        catsubset = ProductCategorySubset.objects.get(active=True, slug=Subset)

                        #create new Product object for saving data
                        product_object = Product.objects.create(
                            Brand = brand,
                            ProductCategorySubset = catsubset,
                            faName = fa_name,
                            enName = en_name,
                            code = code,
                            poster = poster,
                            J_addition_datetime = jdatetime.date.today(),
                            J_editition_datetime = jdatetime.date.today(),
                            review = review,
                            tags = tags,
                            url = url,
                            )

                        #create new product image object for other images
                        images = request.FILES.getlist('image', 'null')
                        for image in images:
                            productimage_object = ProductImage.objects.create(
                                Product = product_object,
                                enName = product_object.enName,
                                image = image,
                            )

                        # #create Features
                        counter = int(request.POST.get('counter', 'null'))
                        for number in range(counter):
                            featurecatname = 'FeatureCats-'+str(int(number)+1)
                            keyname = 'key-'+str(int(number)+1)
                            valuename = 'value-'+str(int(number)+1)
                            importantname = 'important-'+str(int(number)+1)
                            featureCat = request.POST.get(featurecatname, 'null')

                            featurecat_object = FeaturesCategories.objects.get(active=True, name=featureCat)
                            
                            key = request.POST.get(keyname, 'null')
                            print(key)
                            print('key')
                            
                            value = request.POST.get(valuename, 'null')
                            print(value)
                            print('value')

                            important = request.POST.get(importantname, 'null')
                            
                            if important == 'on':
                                important = True
                            if important == 'null':
                                important = False

                        
                            feature_object = Feature.objects.create(
                                Product = product_object,
                                FeaturesCategories = featurecat_object,
                                feature = key,
                                descriptions = value,
                                important = important,
                            )


                        #create new Tag object for saving data
                        taglist = tags.split(',')
                        for tag in taglist :
                            #if this tags are exists just add one unit to number of used 
                            if ProductTag.objects.filter(active=True, name=tag).exists():
                                producttagObject = ProductTag.objects.get(active=True, name=tag)
                                numberOfUsed = producttagObject.numberOfUsed
                                producttagObject.numberOfUsed = numberOfUsed + 1
                                producttagObject.save()
                            #create new Tag object if this tag is new
                            else:
                                ProductTag.objects.create(
                                    name = tag
                                )

        context = {
            'title':PageTitle,
            'tagid':tagid,
            'admin_login':login_object,
            'admin_info':info_object,
            'pform':product_form,
            'iform':productImage_form,
            'brands':brands_objects,
            'catsubsets':catsubsets_object,
            'featureCats':FeaturesCategories_objects,
            'featureCat_status' :FeaturesCategories_status,
        }

    return render(request, 'adminstrator/dashboard/product/add_product.html', context)


def edit_product(request, slug):
    # if you dont have this session come back
    if 'admin_login_username' not in request.session:
            return redirect('admin_login')
    else:
        admin_username = request.session['admin_login_username']

        PageTitle = 'اضافه کردن محصول'
        tagid = 'products'

        # Get the admin objects 
        login_object = AdminLogin.objects.none()
        info_object = AdminInfo.objects.none()
        product_object = Product.objects.none()
        brands_object = Brand.objects.none()
        subset_object = ProductCategorySubset.objects.none()
        images_object = ProductImage.objects.none()
        features_object = Feature.objects.none()
        featureCats_object = FeaturesCategories.objects.none()


        product_status = 404
        brand_status = 404
        subset_status = 404
        images_status = 404
        features_status = 404
        featureCats_status = 404

        if AdminLogin.objects.filter(username=admin_username).exists():
            login_object = AdminLogin.objects.get(username=admin_username)
            if AdminInfo.objects.filter(AdminLogin=login_object).exists(): 
                info_object = AdminInfo.objects.get(AdminLogin=login_object)

                # add blog_form to variable for send to front
                product_form = Product_form()
                productImage_form = ProductImage_form()

                if Product.objects.filter(slug=slug, active=True).exists():
                    product_object = Product.objects.get(slug=slug, active=True)
                    product_status = 200

                    if Brand.objects.filter(active=True).exists():
                        brands_object = Brand.objects.filter(active=True).exclude(en_name=product_object.Brand.en_name)
                        brand_status = 200

                    if ProductCategorySubset.objects.filter(active=True).exists():
                        subset_object = ProductCategorySubset.objects.filter(active=True).exclude(slug=product_object.ProductCategorySubset.slug)
                        subset_status = 200

                    # add product_form to variable for send to front
                    product_form = Product_form(instance = product_object)
                    # productImage_form = ProductImage_form() 

                    if ProductImage.objects.filter(active=True, Product=product_object).exists():
                        images_object = ProductImage.objects.filter(active=True, Product=product_object)
                        images_status  = 200

                    if Feature.objects.filter(active=True, Product=product_object).exists():
                        features_object = Feature.objects.filter(active=True, Product=product_object)
                        features_status = 200
                        featurescounter = 0
                        objwehave = ''
                        for feature_object in features_object:
                            featurescounter += 1
                            objwehave += str(feature_object.id) 

                        if FeaturesCategories.objects.filter(active=True).exists():
                            featureCats_object = FeaturesCategories.objects.filter(active=True)
                            featureCats_status = 200


                    if request.POST :
                        if 'editproductBTN' in request.POST:
                            brand = request.POST.get('brand', 'null')
                            Subset = request.POST.get('Subset', 'null')
                            code = request.POST.get('code', 'null')
                            fa_name = request.POST.get('fa_name', 'null')
                            en_name = request.POST.get('en_name', 'null')
                            url = request.POST.get('url', 'null')
                            tags = request.POST.get('tags', 'null')
                            review = request.POST.get('review', 'null')
                            poster = request.FILES.get('poster', 'null')

                            brand = Brand.objects.get(active=True, en_name=brand)
                            catsubset = ProductCategorySubset.objects.get(active=True, slug=Subset)

                            # update new Product object for saving data
                            product_object.Brand = brand
                            product_object.ProductCategorySubset = catsubset
                            product_object.code = code
                            product_object.faName = fa_name
                            product_object.enName = en_name
                            product_object.url = url
                            product_object.tags = tags
                            product_object.review = review
                            if poster != 'null':
                                product_object.poster = poster
                            product_object.J_editition_datetime = jdatetime.date.today()
                            product_object.save()


                            # update new product image object for other images
                            images = request.FILES.getlist('image', 'null')
                            if images != 'null':
                                for image in images:
                                    productimage_object = ProductImage.objects.create(
                                        Product = product_object,
                                        enName = product_object.enName,
                                        image = image,
                                    )

                            # update Features
                            newcounter = int(request.POST.get('counter', 'null'))
                            newobjwehave = request.POST.get('objwehave', 'null')
                            print(newobjwehave)

                            for feature_id in newobjwehave:
                                featurecatname = 'FeatureCats-' + feature_id
                                keyname = 'key-' + feature_id
                                valuename = 'value-' + feature_id
                                importantname = 'important-' + feature_id

                                featureinput =  request.POST.get(featurecatname, 'null')
                                keyinput =  request.POST.get(keyname, 'null')
                                valueinput =  request.POST.get(valuename, 'null')
                                important = request.POST.get(importantname, 'null')
                                if important == 'on':
                                    important = True
                                if important == 'null':
                                    important = False

                                if Feature.objects.filter(active=True, id=feature_id).exists():
                                        featureCat_object = Feature.objects.get(active=True, id=feature_id)
                                        # update featureCat
                                        if featureinput != '':
                                            if FeaturesCategories.objects.filter(active=True, name=featureinput).exists():
                                                FeaturesCategories_object = FeaturesCategories.objects.get(active=True, name=featureinput)

                                                featureCat_object.FeaturesCategories = FeaturesCategories_object
                                        
                                        featureCat_object.feature = keyinput
                                        featureCat_object.descriptions = valueinput
                                        featureCat_object.important = important
                                        featureCat_object.save()

                                else:
                                    if FeaturesCategories.objects.filter(active=True, name=featureinput).exists():
                                        FeaturesCategories_object = FeaturesCategories.objects.get(active=True, name=featureinput)
                                       
                                        Feature.objects.create(
                                            Product = product_object,
                                            FeaturesCategories = FeaturesCategories_object,
                                            feature = keyinput,
                                            descriptions = valueinput,
                                            important = important,
                                        )
                            
                            # update tags
                                # previous tags proccess
                            # previous_tags = product_object.tags
                            # pervtaglist = previous_tags.split(',')
                            
                            #     # new tags proccess
                            # for tag in taglist:
                                

                                
                        return redirect('/v1/adminstrator/dashboard/edit_product/'+product_object.slug)


        context = {
            'title':PageTitle,
            'tagid':tagid,

            'product' :product_object,
            'product_status' :product_status,

            'brands' :brands_object,
            'brand_status' :brand_status,

            'subsets' :subset_object,
            'subset_status' :subset_status,

            'pform' :product_form,

            'images' :images_object,
            'images_status' :images_status,

            'features' :features_object,
            'feature_status' :features_status,
            'featurescounter' :featurescounter,
            'objwehave' :objwehave,
            'featureCats' :featureCats_object,
            'featureCats_status' :featureCats_status,
        }


    return render(request, 'adminstrator/dashboard/product/edit_product.html', context)

def deActive_product(request, slug):

    product_object = Product.objects.none()
    # productimage_object = ProductImage.objects.none()
    # feature_object = Feature.objects.none()
    # producttag_object = ProductTag.objects.none()

    if Product.objects.filter(active=True, slug=slug).exists():
        product_object = Product.objects.get(active=True, slug=slug)

        # if ProductImage.objects.filter(active=True, Product=product_object).exists():
        #     productimage_object = ProductImage.objects.filter(active=True, Product=product_object)
        #     for image in productimage_object:
        #         image.active = False
        #         image.save()
        


        product_object.active = False
        product_object.save()

    return redirect('/v1/adminstrator/dashboard/manage_products/')