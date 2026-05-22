from django.shortcuts import redirect, render
from .models import Order, Supplier, Product, Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# -----------------LANDING AFTER LOGIN--------------
def landingview(request):
    return render(request, 'landingpage.html')



# ----------------LOGIN AND LOGOUT-----------------
def loginview(request):
    return render(request, 'loginpage.html')


def login_action(request):
    user = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = user, password = password)
    if user:
        login(request, user)
        context = {'name': user.first_name}
        return render(request, "landingpage.html", context) #
    else:
        return render(request, "loginerror.html")


def logout_action(request):
    logout(request)
    return render(request, "loginpage.html")



# -------------------------------Product views---------------------------------------------------
# def productlistview(request):
#     if not request.user.is_authenticated:
#         return render(request, 'loginpage.html')
#     else:
#         productlist = Product.objects.all()
#         supplierlist = Supplier.objects.all()
#         context = {'products': productlist, 'suppliers': supplierlist}
#         return render(request, 'productlist.html', context)

@login_required(login_url='/login/')
def productlistview(request):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productlist, 'suppliers': supplierlist}
    return render(request, 'productlist.html', context)


# -------------Search products--------------
def search_products(request):
    search = request.POST.get('search')
    filtered = Product.objects.filter(productname__icontains=search)
    context = {'products': filtered}
    return render(request, 'productlist.html', context)


 # --------------Add product-----------------
def addproduct(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST.get('productname')
        b = request.POST.get('packagesize')
        c = request.POST.get('unitprice')
        d = request.POST.get('unitsinstock')
        e = request.POST.get('supplier')
    
        Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
        return redirect(request.META['HTTP_REFERER'])
    

# ----------------Edit product-----------------
def edit_product_get(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render(request, 'edit_product.html', context)

# ----------------Edit product save-----------------
def edit_product_post(request, id):
    item = Product.objects.get(id = id)
    item.unitprice = request.POST['unitprice']
    item.unitsinstock = request.POST['unitsinstock']
    item.save()
    return redirect(productlistview)


 # -------------Delete product--------------
def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render(request,"confirmdelprod.html",context)


def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return redirect(productlistview)


# --------------Filter products by supplier--------------
def products_filtered(request, id):
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts}
    return render (request,"productlist.html",context)



# ------------------------------------Supplier views---------------------------------------------------
@login_required(login_url='/login/')
def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render(request, 'supplierlist.html', context)


# --------------Search suppliers--------------
def search_suppliers(request):
    search = request.POST.get('search')
    filtered = Supplier.objects.filter(companyname__icontains=search)
    context = {'suppliers': filtered} 
    return render(request, 'supplierlist.html', context)


 # -------------Add supplier----------------
def addsupplier(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    a = request.POST.get('companyname')
    b = request.POST.get('contactname')
    c = request.POST.get('address')
    d = request.POST.get('phone')
    e = request.POST.get('email')
    f = request.POST.get('country')
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])


# ----------------Edit supplier-----------------
def edit_supplier_get(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render(request, 'edit_supplier.html', context)


# ----------------Edit supplier save-----------------
def edit_supplier_post(request, id):
    supplier = Supplier.objects.get(id = id)
    supplier.companyname = request.POST['companyname']
    supplier.contactname = request.POST['contactname']
    supplier.address = request.POST['address']
    supplier.phone = request.POST['phone']
    supplier.email = request.POST['email']
    supplier.country = request.POST['country']
    supplier.save()
    return redirect(supplierlistview)


# -------------Delete supplier--------------
def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"confirmdelsuppl.html",context)

def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)



# ------------------------------------Customers views------------------------------------------------------
@login_required(login_url='/login/')
def customerlistview(request):
    customerlist = Customer.objects.all()
    context = {'customers': customerlist}
    return render(request, 'customerlist.html', context)


# -------------Search customers--------------
def search_customers(request):
    search = request.POST.get('search')
    filtered = Customer.objects.filter(companyname__icontains=search)
    context = {'customers': filtered}
    return render(request, 'customerlist.html', context)


# --------------Add customer----------------
def addcustomer(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    a = request.POST.get('companyname')
    b = request.POST.get('contactname')
    c = request.POST.get('address')
    d = request.POST.get('phone')
    e = request.POST.get('email')
    f = request.POST.get('country')
    Customer(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])


# ----------------Edit customer-----------------
def edit_customer_get(request, id):
    customer = Customer.objects.get(id = id)
    context = {'customer': customer}
    return render(request, 'edit_customer.html', context)

# ----------------Edit customer save-----------------
def edit_customer_post(request, id):
    customer = Customer.objects.get(id = id)
    customer.companyname = request.POST['companyname']
    customer.contactname = request.POST['contactname']
    customer.address = request.POST['address']
    customer.phone = request.POST['phone']
    customer.email = request.POST['email']
    customer.country = request.POST['country']
    customer.save()
    return redirect(customerlistview)


# -------------Delete customer--------------
def confirmdeletecustomer(request, id):
    customer = Customer.objects.get(id = id)
    context = {'customer': customer}
    return render(request, 'confirmdelcust.html', context)

# -------------Delete customer save--------------
def deletecustomer(request, id):
    Customer.objects.get(id = id).delete()
    return redirect(customerlistview)



# ----------------------------------------Orders views----------------------------------------------------

@login_required(login_url='/login/')
def orderlistview(request):
    orderlist = Order.objects.all()
    customers = Customer.objects.all()
    suppliers = Supplier.objects.all()
    products = Product.objects.all()
    context = {'orders': orderlist, 'customers': customers, 'suppliers': suppliers, 'products': products}
    return render(request, 'orderlist.html', context)


# -------------Search orders--------------
def search_orders(request):
    search = request.POST.get('search')
    filtered = Order.objects.filter(orderdate__icontains=search)
    context = {'orders': filtered, 'customers': Customer.objects.all(), 'suppliers': Supplier.objects.all(), 'products': Product.objects.all()}
    return render(request, 'orderlist.html', context)


# -------------Add order----------------
def addorder(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    a = request.POST.get('customer')
    b = request.POST.get('product')
    c = request.POST.get('orderdate')
    d = request.POST.get('requireddate')
    e = request.POST.get('supplier')
    Order(customer = Customer.objects.get(id = a), product = Product.objects.get(id = b), orderdate = c, requireddate = d, 
          supplier = Supplier.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])


#-------------Edit order-----------------

def edit_order_get(request, id):
    order = Order.objects.get(id = id)
    context = {'order': order, 'suppliers': Supplier.objects.all(), 'products': Product.objects.all()}
    return render(request, 'edit_order.html', context)

# ----------------Edit order save-----------------
def edit_order_post(request, id):
    order = Order.objects.get(id = id)
    order.product = Product.objects.get(id = request.POST['product'])
    order.orderdate = request.POST['orderdate']
    order.requireddate = request.POST['requireddate']
    order.supplier = Supplier.objects.get(id = request.POST['supplier'])
    order.save()
    return redirect(orderlistview)


# -------------Delete order--------------

def confirmdeleteorder(request, id):
    order = Order.objects.get(id = id)
    context = {'order': order}
    return render(request,"confirmdelorder.html",context)


def deleteorder(request, id):
    Order.objects.get(id = id).delete()
    return redirect(orderlistview)



# -------------Filter orders by customer--------------
def orders_by_customer(request, customer_id):
    filteredorders = Order.objects.filter(customer=customer_id)
    context = {'orders': filteredorders}
    return render(request, "orderlist.html", context)











