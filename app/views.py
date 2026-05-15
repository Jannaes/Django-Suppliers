from django.shortcuts import redirect, render
from .models import Supplier, Product
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



# ----------------Product views-----------------
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


 # -------------Delete product--------------
def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render(request,"confirmdelprod.html",context)


def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return redirect(productlistview)


 # ----------------Edit product-----------------
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


# --------------Filter products by supplier--------------
def products_filtered(request, id):
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts}
    return render (request,"productlist.html",context)


# ----------------Supplier views-----------------
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
    a = request.POST.get('companyname')
    b = request.POST.get('contactname')
    c = request.POST.get('address')
    d = request.POST.get('phone')
    e = request.POST.get('email')
    f = request.POST.get('country')
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])


# -------------Delete supplier--------------
def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"confirmdelsuppl.html",context)

def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)


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



