from typing import Any
from django.shortcuts import render,redirect
from suppliers.models import Suppliers
from rest_framework.views import APIView #type:ignore
from django.http import JsonResponse,HttpResponse
from django.views.generic.base import TemplateView
from customer.models import Customer
from django.shortcuts import render, get_object_or_404
from .models import Suppliers
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from medicine.models import Medicine
from orders.models import Orders

# Create your views here.

def seller(request,cid):
    customer_id = request.GET.get('cid')  # Or however you obtain the supplier_id
    return render(request, 'suppliers/sell.html', {"Customer_id": customer_id,'currentUser':request.session['user_name'],'currentUserId':request.session['customer_id'],'count':request.session['count']})

def medicine(request):
    customer_id = request.GET.get('cid')  # Or however you obtain the supplier_id
    return render(request, 'medicine/medicine.html', {"C_id": customer_id})
def viewallsellers(request):
    sellers = Suppliers.objects.all()
    return render(request, 'suppliers/allsellers.html',{'sellers':sellers} )
def dashboard(request):
    return render(request, 'suppliers/dashboard.html' )
def sellerbilling(request):
    orders = Orders.objects.all()
    context = {
        'ordersall':orders
    }
    return render(request, 'suppliers/sellerbilling.html' ,context)
def products(request):
    medicine = Medicine.objects.all()
    context = {
        'medicineall':medicine
    }
    return render(request, 'suppliers/products.html' ,context)
# view for seller
def sellIndex(request):
    return render(request, 'customer/index.html',{'supplier':request.session['supplier_id']})

class CreateSeller(APIView):
    def post(self, request):
        # Use `get` to safely access the values, with None or a default value if the key is missing
        sname = request.data.get('sellername', None)
        semail = request.data.get('selleremail', None)
        sphone = request.data.get('sellerphone', None)
        scomp = request.data.get('sellercompany', None)
        sgst = request.data.get('sellergstNo', None)
        sadd = request.data.get('selleraddress', None)
        scid = request.data.get('customer_id', None)  # Retrieve customer ID from request data
        # Check if `scid` is provided and get the corresponding customer
        if scid:
            try:
                customer = Customer.objects.get(cid=scid)
            except Customer.DoesNotExist:
                return JsonResponse({"status": "fail", "message": "Customer not found"}, status=404)
        else:
            return JsonResponse({"status": "fail", "message": "Customer ID not provided"}, status=400)

        # Create and save the supplier instance
        supplier = Suppliers()
        supplier.supplier_name = sname
        supplier.email = semail
        supplier.phone_number = sphone
        supplier.CompanyName = scomp
        supplier.CompanyGst = sgst
        supplier.address = sadd
        supplier.cid = customer
        supplier.account_created_by = 'Company'
        supplier.save()

        request.session['supplier_id'] = supplier.supplier_id
        supplier_id = request.session['supplier_id']
        if not supplier_id:
            return HttpResponse("Before Continuing You have to create a seller Account")
        return JsonResponse({"status": "pass",'supplier_id':supplier_id} )



def view_seller(request):
    supplier = Suppliers()
    sid = supplier.supplier_id
    # Redirect to another view (e.g., seller_dashboard) with supplier_id
    return redirect('seller_dashboard', supplier_id = sid,)

def seller_dashboard(request, supplier_id):
    supplier = get_object_or_404(Suppliers, supplier_id=supplier_id)
    medicine = Medicine.objects.filter(supplier_id = supplier)
  
    context = {
        'sellerdata': supplier,
        'medicines':medicine,
        'currentUser':request.session['user_name'],

    }
    return render(request, 'suppliers/dashboard.html', context)

def seller_accounts(request):
    cid = request.GET.get('cid')
    supplierdata = Suppliers.objects.all()
    context = {
        'supplier_data':supplierdata,
    }
    return render(request, 'suppliers/sellerdashboard.html', context)
    
class ViewSeller(TemplateView):
    template_name = 'customer/index.html'
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        supplier_id = self.request.session.get('supplier_id')
        return JsonResponse({'supplier':supplier_id})
class delete_view(APIView):
    def post(self, request):
        sid = request.POST['supplier_id']
        Suppliers.objects.filter(sid = sid).delete()
        return JsonResponse({"status":"pass"})
