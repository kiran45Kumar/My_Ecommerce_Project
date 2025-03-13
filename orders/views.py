from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, Medicine
from customer.models import Customer
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from .models import Orders
from suppliers.models import Suppliers
from django.views.generic import TemplateView
# Create your views here.
def order(request):
    orders = Orders.objects.all()
    context = {
        'ordersall':orders
    }
    return render(request, 'orders/order.html',context )
def cart(request):
    return render(request, 'orders/cart.html')
def checkout(request):
    return render(request,'orders/checkout.html')
def new(request):
    return render(request,'orders/new.html')    
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, Medicine
from customer.models import Customer


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Cart, Medicine, Customer
def add_to_cart(request):
    if request.method == 'POST':
        medicine_id = request.POST.get('medicine_id')
        quantity = request.POST.get('quantity')
        customer_id = request.POST.get('customer_id')

        try:
            medicine = Medicine.objects.get(med_id=medicine_id)

            # Get the customer associated with the customer_id
            customer = get_object_or_404(Customer, cid=customer_id)

            # Create a cart entry
            Cart.objects.create(
                cid=customer,  # Assign the customer instance here
                medicine=medicine,
                quantity=quantity
            )
            return JsonResponse({'status': 'success'})
        except Medicine.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Medicine not found'})
        except Customer.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Customer not found'})
    
    return JsonResponse({'status': 'fail', 'message': 'Invalid request method'})
def add_to_order(request):
      if request.method == 'POST':
        medicine_id = request.POST.get('medicine_id')
        quantity = request.POST.get('quantity')
        customer_id = request.POST.get('customer_id')

        try:
            # Get the medicine
            medicine = Medicine.objects.get(med_id=medicine_id)

            # Get the customer associated with the customer_id
            customer = get_object_or_404(Customer, cid=customer_id)

            # Create a cart entry
            Orders.objects.create(
                cid=customer,  # Assign the customer instance here
                product=medicine,
                quantity=quantity
            )
            return JsonResponse({'status': 'success'})
        except Medicine.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Medicine not found'})
        except Customer.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Customer not found'})
    
      return JsonResponse({'status': 'fail', 'message': 'Invalid request method'})

def cart_page(request, cid):
    cart_items = Cart.objects.filter(cid=cid)
    total_price = sum(item.medicine.price * item.quantity for item in cart_items)
    if request.method == 'POST':
        action = request.POST.get('action')
        cart_item_id = request.POST.get('cart_item_id')
        cart_item = get_object_or_404(Cart, id=cart_item_id)
        if action == 'increment':
            cart_item.quantity += 1
        elif action == 'decrement' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()
        customer_id = request.session.get('customer_id')
        cart = Cart.objects.filter(cid=customer_id)
        request.session['count'] =  cart.count()
        total_price = sum(item.medicine.price * item.quantity for item in cart_items)
        return JsonResponse({
            'quantity': cart_item.quantity,
            'total_price': total_price,
        })
        
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'currentUser':request.session['user_name'],
        'currentUserId':request.session['customer_id'],
        'count':   request.session['count'] 
    }
    return render(request, 'orders/checkout.html', context)
from django.views.decorators.http import require_POST
def display(request,cid,med_id):
    allmed = Medicine.objects.get(med_id = med_id)
    allcustomers = Customer.objects.all()
    allsuppliers = Suppliers.objects.all()
    return render(request, 'orders/display.html',{'allmed':allmed, 'allcustomer':allcustomers,'allsupplier':allsuppliers,'currentUserId':request.session['customer_id'],'currentUser':request.session['user_name'],'count':request.session['count'],'currentUserEmail':request.session['customer_email']})
@require_POST
def update_cart(request):
    medicine_id = request.POST.get('med_id')
    action = request.POST.get('action')
    
    if not medicine_id or not action:
        return JsonResponse({'error': 'Invalid request parameters'}, status=400)

    cart_item = get_object_or_404(Cart, medicine_id=medicine_id)
    if action == 'increment':
        cart_item.quantity += 1
    elif action == 'decrement' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    else:
        return JsonResponse({'error': 'Invalid action'}, status=400)
    
    cart_item.save()
    total_price = cart_item.medicine.price * cart_item.quantity
    
    return JsonResponse({
        'new_quantity': cart_item.quantity,
        'total_price': total_price
    })
from django.http import JsonResponse
from .models import Orders, Medicine, Customer, Suppliers

from django.utils import timezone
from .models import Orders, Customer, Medicine
from rest_framework.views import APIView
from django.http import JsonResponse

class order_cart(APIView):
    def post(self, request):
        med_id = request.data.get('med_id')
        user_id = request.data.get('user_id')
        user_name = request.data.get('user_name')
        user_phone = request.data.get('user_phone')
        user_email = request.data.get('user_email')
        user_address = request.data.get('user_address')
        user_alternate_phone = request.data.get('user_alternate_phone')
        user_landmark = request.data.get('user_landmark')
        user_city = request.data.get('user_city')
        user_state = request.data.get('user_state')
        user_postal_code = request.data.get('user_postal_code')
        credit_card_number = request.data.get('credit_card_number')
        cvv = request.data.get('cvv')
        expiry = request.data.get('expiry')

        customer = Customer.objects.get(cid=user_id)
        product = Medicine.objects.get(med_id=med_id)
        
        order = Orders.objects.create(
            cid=customer,
            product=product,
            user_name=user_name,
            user_phone=user_phone,
            user_email=user_email,
            user_address=user_address,
            user_alternate_phone=user_alternate_phone,
            user_landmark=user_landmark,
            user_city=user_city,
            user_state=user_state,
            user_postal_code=user_postal_code,
            credit_card_number=credit_card_number,
            cvv=cvv,
            expiry_date=expiry,
            total_amount=100 
        )
        
        # Update the status based on elapsed time
        elapsed_time = timezone.now() - order.order_date
        elapsed_minutes = elapsed_time.total_seconds() / 60 
        if elapsed_minutes >= 12:
            order.status = 'DELIVERED'
        elif elapsed_minutes >= 9:
            order.status = 'DISPATCHED'
        elif elapsed_minutes >= 6:
            order.status = 'SHIPPED'
        elif elapsed_minutes >= 3:
            order.status = 'ORDERED'
        else:
            order.status = 'PENDING'

        order.save()
        
        request.session['order_id'] = order.order_id
        
        return JsonResponse({'status': "pass", 'currentUserId': request.session['customer_id']})

import datetime
from django.utils import timezone
from .models import Orders, Suppliers
def orderPlaced(request):
     customer_id = request.session.get('customer_id')
     orders = Orders.objects.filter(cid=customer_id)
     context = {
         "userOrder":orders,
         'currentUserId': request.session['customer_id']
     }
     return render(request, 'orders/orderplace.html', context)
class ViewOrders(TemplateView):
    template_name = 'orders/new.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_id = self.request.session.get('customer_id')
        orders = Orders.objects.filter(cid=customer_id)
        suppliers = Suppliers.objects.all()
        context = {
            'allorders': orders,
            'all_suppliers': suppliers,
            'currentUser': self.request.session.get('user_name'),
            'currentUserId': customer_id,
            'count': self.request.session.get('count', 0)
        }
        return context

class DeleteCart(APIView):
    def post(self, request):
        id = request.POST['id']
        Cart.objects.filter(id = id).delete()
        return JsonResponse({"status":"pass"})
class Deleteorder(APIView):
    def post(self, request):
        id = request.POST['id']
        Orders.objects.filter(order_id = id).delete()
        return JsonResponse({"status":"pass"})