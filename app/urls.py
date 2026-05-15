"""
URL configuration for suppliers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import edit_product_get, edit_product_post, edit_supplier_get, edit_supplier_post, \
    landingview, login_action, loginview, logout_action, \
    productlistview, products_filtered, search_products, search_suppliers, supplierlistview, addsupplier, addproduct, \
    confirmdeleteproduct, deleteproduct, confirmdeletesupplier, deletesupplier

urlpatterns = [

    # ------------Landing page after login-------------
    path('', landingview),


    # --------Loginview and authentication method------------   
    path('login/', loginview),
    path('login-action/', login_action),
    path('logout/', logout_action),


    # ------------- Products URLs--------------
    path('products/', productlistview),
    path('search-products/', search_products),
    path('add-product/', addproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('products-by-supplier/<int:id>/', products_filtered),

     # ------------- Suppliers URLs--------------
    path('suppliers/', supplierlistview),
    path('search-suppliers/', search_suppliers),
    path('add-supplier/', addsupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),



]
