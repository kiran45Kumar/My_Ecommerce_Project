from django.shortcuts import render, redirect
from .models import Customer, ContactForm, DeliveryPincode
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.http import JsonResponse, HttpResponse,Http404
from django.contrib.auth import authenticate, login as auth_login
from rest_framework.views import APIView # type: ignore
from medicine.models import Medicine
from orders.models import Orders
from orders.models import Cart
from suppliers.models import Suppliers
import requests

# Signup View
def signup(request):
    return render(request, 'customer/signup.html')
# Login View
def login(request):
    return render(request, 'customer/login.html')
# Contact View
def contact(request):
    return render(request, 'customer/contact.html',{'currentUser':request.session['user_name'],'currentUserId':request.session['customer_id'],'count':request.session['count'],'currentUserEmail':request.session['customer_email']})
def userdashboard(request,name, cid):
    customer_id = request.session['customer_id']
    customer = Customer.objects.filter(cid = customer_id)
    # request.session['customer_phone'] = customer.phone
    return render(request, 'customer/dashboard.html',{'customer':customer,'currentUser':request.session['user_name'],'currentUserId':request.session['customer_id'],'count':request.session['count'],'currentUserEmail':request.session['customer_email']})

# Login Check View
class LoginCheck(APIView):
    def post(self, request):
        email_1 = request.POST['mail'] # Using request.data if POST data is sent as JSON
        password_1 = request.POST['passw']
        customer = Customer.objects.get(email = email_1)
        try:
            # Query by email or any unique field instead of password
            if Customer.objects.filter(email = email_1, password = password_1).exists():
                request.session['user_name'] = customer.name
                request.session['customer_id'] = customer.cid
                
                request.session['customer_email'] = email_1 
                return JsonResponse({"status":"pass","name":customer.name,'cid':customer.cid,"role":customer.role,'email':customer.email})
            else:
                 return JsonResponse({"status":"fail", "message":"Invalid Credentials"})
        
        except Customer.DoesNotExist:
            # Handle case when no customer is found with the provided email
            return JsonResponse({"status": "fail", "failure": "Account does not exist Please Signup"})

        return HttpResponse("Success")

def logout(request):
    request.session.pop('user_name', None)
    request.session.pop('customer_id', None)
    return render(request, 'customer/logout.html')

def index(request,cid):
    user_name = request.GET.get('name', 'Guest')  # Default to 'Guest' if no name is provided
    cust_id = request.GET.get('cid')
    medicines = Medicine.objects.all()[:5]
    customer_id = request.session.get('customer_id')
    cart_count = Cart.objects.filter(cid=customer_id).count()
    contact_issues = ContactForm.objects.filter(cid = customer_id)
    delivery = DeliveryPincode.objects.filter(user_id = customer_id)
    request.session['count'] = cart_count
    return render(request, 'customer/index.html', {'user_name': user_name,"customer":cust_id,'medicines':medicines,'currentUser':request.session['user_name'],'currentUserId':request.session['customer_id'], 'count':request.session['count'],"delivery":delivery})
# Signup API View
class CreateUser(APIView):
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        phone = request.POST['phone']
        role = request.POST['role']
        fname = request.POST['fname']
        lname = request.POST['lname']
        if Customer.objects.filter(email=email).exists():
            return JsonResponse({"status": "fail", "message": "Email already exists"})
        user = Customer()
        user.email = email
        user.password = password 
        user.first_name = fname
        user.last_name = lname
        user.name = name
        user.phone = phone
        user.role = role
        user.save()
        return JsonResponse({"status": "pass"})
class ContactBox(APIView):
    def post(self, request):
        contactid = request.POST['contactid']
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        cmessage = request.POST['cmessage']
        if not cmessage:
            return JsonResponse({"message":"Please Enter your issues"})
        else:
            message = "Thanks for Submitting"
        customer = Customer.objects.get(cid = contactid)
        contact = ContactForm()
        contact.cid = customer
        contact.contact_name = cname
        contact.contact_email = cemail
        contact.contact_message = cmessage
        contact.save()
        return JsonResponse({"status": "pass","success":message})
def products(request):
     medicines = Medicine.objects.all()
     context = {
         "medicines":medicines,
     }
     return render(request, 'customer/product.html', context)
def seller(request):
    supplier = Suppliers.objects.all()
    context = {
         "supplier":supplier,
     }
    return render(request, 'customer/seller.html', context)
def admin(request):
    customer = Customer.objects.all()
    medicines = Medicine.objects.all()
    orders = Orders.objects.all()
    cart = Cart.objects.all()
    contact = ContactForm.objects.all()
    context = {
        "customer":customer,
        "medicines":medicines,
        "orders":orders,
        "cart":cart,
       "contact":contact
    }
    return render(request, 'customer/admin.html', context)
def exampleview(request):
     contact = ContactForm.objects.all()
     context = {
       "contacts":contact
     }
     return render(request, 'customer/example.html',context)
def seller(request):
    suppliers = Suppliers.objects.all()
    return render(request, 'customer/supplier.html',{'suppliers':suppliers})
def billing(request):
    return render(request, 'customer/billing.html')
def delivery(request):
    orders = Orders.objects.all()
    context = {
        "orders":orders
    }
    return render(request, 'customer/delivery.html',context)

def terms(request):
    return render(request, 'customer/terms.html')
from django.http import JsonResponse
from django.views import View
# update user details
class UpdateUser(APIView):
    def post(self, request):
        try:
            id = request.POST.get('id')
            username = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            password = request.POST.get('password')
            customer = Customer.objects.get(cid=id)
            customer.name = username
            customer.email = email
            customer.phone = phone
            customer.first_name = fname
            customer.last_name = lname
            customer.password = password
            customer.save()
        except Customer.DoesNotExist:
            return JsonResponse({"status": "fail", "error": "Customer not found"})
        except Exception as e:
            return JsonResponse({"status": "fail", "error": str(e)})
        return JsonResponse({"status": "pass"})

# Delete User API View
class delete_user(APIView):
    def post(self, request):
        id = request.POST['cid']
        Customer.objects.filter(cid=id).delete()
        return JsonResponse({"status": "pass"})

# View User Class-Based View
class ViewUser(TemplateView):
    template_name = 'view.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userdata = Customer.objects.all()
        med_data = Medicine.objects.all()
        context = {'userdata':userdata, "med_data":med_data,'currentUser':self.request.session.get('user_name')}
        return context
def issues(request):
    customer_id = request.session.get('customer_id')
    contact_issues = ContactForm.objects.filter(cid = customer_id)
    context = {"contact_issues":contact_issues,'currentUser':request.session['user_name']}
    return render(request, 'customer/issues.html',context)
class delete_account(APIView):
    def post(self, request):
        id = request.POST['id']
        Customer.objects.filter(cid = id).delete()
        return JsonResponse({"status":"pass"})
class GetRegion(APIView):
    def post(self, request):
        pincode = request.POST.get('pincode')
        customer_id = request.POST.get('customer_id')
        response = requests.get(f'https://api.postalpincode.in/pincode/{pincode}')
        data = response.json()
        if data[0]['Status'] == 'Success': 
            region = data[0]['PostOffice'][0]['District']

            user = Customer.objects.get(cid = customer_id)
            DeliveryPincode.objects.update_or_create(user_id = user, pincode = pincode, defaults={'region':region})
            return JsonResponse({"status":"success","region":region})
        else:
            return JsonResponse({"status":"error","message":"Invalid Pincode"})
def admin_dashboard(request):
    return render(request, 'admin/index.html')
def form_element_input(request):
    return render(request, 'admin/form-element-input.html')
def billing(request):
    return render(request, 'admin/billing.html')