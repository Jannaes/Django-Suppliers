from django.shortcuts import redirect, render

from .models import Supplier, Product

def landingview(request):
    return render(request, 'landingpage.html')


# Product views
def productlistview(request):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productlist, 'suppliers': supplierlist}
    return render(request, 'productlist.html', context)


 # Add product view
def addproduct(request):
    a = request.POST['productname']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['supplier']
    
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])


 # Delete product view
def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render (request,"confirmdelprod.html",context)


def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return redirect(productlistview)


# Delete supplier view
def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"confirmdelsuppl.html",context)


def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)



# Supplier views
def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render(request, 'supplierlist.html', context)


 # Add supplier view
def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])




