from django.urls import path, include
from . import views, ajaxdef

urlpatterns = [
    path('login/', views.login, name="admin_login"),
    path('dashboard/', views.dashboard, name="dashboard"),

    path('dashboard/manage_blogs/', views.manage_blogs, name="mng_blogs"),
    path('dashboard/add_blog/', views.add_blog, name="add_blog"),
    path('dashboard/edit_blog/<str:slug>/', views.edit_blog, name="edit_blog"),
    path('dashboard/blog/deActive/<str:slug>/', views.deActive_blog, name='deActive_blog'),

    path('dashboard/manage_brands/', views.manage_brands, name="mng_brands"),
    path('dashboard/add_brand/', views.add_brand, name="add_brand"),
    path('dashboard/edit_brand/<int:id>/', views.edit_brand, name="edit_brand"),
    path('dashboard/brand/deActive/<int:id>/', views.deActive_brand, name='deActive_brand'),

    path('dashboard/manage_pcategories/', views.manage_pcategory, name="mng_pcats"),
    path('dashboard/add_pcategory/', views.add_pcategory, name="add_pcats"),
    path('dashboard/edit_pcategory/<str:slug>/', views.edit_pcategory, name="edit_pcat"),
    path('dashboard/pcategory/deActive/<str:slug>/', views.deActive_pcategory, name='deActive_pcategory'),

    path('dashboard/manage_psubsets/', views.manage_psubset, name="mng_psubsets"), 
    path('dashboard/add_psubset/', views.add_psubset, name="add_psubsets"),
    path('dashboard/edit_psubset/<str:slug>/', views.edit_psubset, name="edit_psubsets"),
    path('dashboard/psubset/deActive/<str:slug>/', views.deActive_psubset, name='deActive_psubset'),

    path('dashboard/add_featurecats/', views.add_featurecats, name="add_featurecats"),

    path('dashboard/manage_products/', views.manage_products, name="mng_products"),
    path('dashboard/add_product/', views.add_product, name="add_product"),
    path('dashboard/edit_product/<str:slug>/', views.edit_product, name="edit_product"),
    path('dashboard/product/deActive/<str:slug>/', views.deActive_product, name='deActive_product'),



    path('dashboard/removepic/', ajaxdef.removepic, name="removepic"),

    path('login/valvalidation/', ajaxdef.account_validation),
]