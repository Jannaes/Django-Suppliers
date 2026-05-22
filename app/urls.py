from django.urls import path

from .views import addorder, edit_product_get, edit_product_post, edit_supplier_get, edit_supplier_post, \
    landingview, login_action, loginview, logout_action, orderlistview, edit_order_get, edit_order_post, \
    confirmdeleteorder, deleteorder, orders_by_customer, productlistview, products_filtered, search_orders, \
    search_products, search_suppliers, supplierlistview, addsupplier, addproduct, \
    confirmdeleteproduct, deleteproduct, confirmdeletesupplier, deletesupplier, customerlistview, \
    addcustomer, search_customers, edit_customer_get, edit_customer_post, confirmdeletecustomer, deletecustomer

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

    # ------------- Customers URLs--------------
    path('customers/', customerlistview),
    path('search-customers/', search_customers),
    path('add-customer/', addcustomer),
    path('confirm-delete-customer/<int:id>/', confirmdeletecustomer),
    path('delete-customer/<int:id>/', deletecustomer),
    path('edit-customer-get/<int:id>/', edit_customer_get),
    path('edit-customer-post/<int:id>/', edit_customer_post),

    # ------------- Orders URLs--------------
    path('orders/', orderlistview),
    path('add-order/', addorder),
    path('edit-order-get/<int:id>/', edit_order_get),
    path('edit-order-post/<int:id>/', edit_order_post),
    path('confirm-delete-order/<int:id>/', confirmdeleteorder),
    path('delete-order/<int:id>/', deleteorder),
    path('search-orders/', search_orders),
    path('orders-by-customer/<int:customer_id>/', orders_by_customer),


]
