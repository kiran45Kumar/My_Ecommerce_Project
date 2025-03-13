from .models import Medicine
from django.shortcuts import render, get_object_or_404,redirect
from suppliers.models import Suppliers
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from customer.models import Customer, DeliveryPincode
# Create your views here.
def medicines(request):
    cid = request.GET.get('cid')  # Use request.GET to get data from the URL query string
    customer = Customer.objects.all()
    customer_id = request.session['customer_id']
    delivery = DeliveryPincode.objects.filter(user_id = customer_id)

    # Fetch medicines data here if needed
    medicines = Medicine.objects.all()  # Assuming you're retrieving all medicines
    
    context = {
        "customerId": cid,
        "customerall": customer,
        "med_data": medicines,  # Include the medicine data
        'currentUser':request.session['user_name'],
        'currentUserId':request.session['customer_id'],
        'count':request.session['count'],
        'delivery':delivery,
        }
    
    return render(request, 'medicine/medicine.html', context)



def create(request):
    supplier_id = request.POST.get('supplier_id')  # Or however you obtain the supplier_id
    return render(request, 'medicine/create.html', {'Supplier_id':supplier_id})



class CreateMedicine(APIView):
    def post(self, request):
        # Use `get` to safely access the values, with None or a default value if the key is missing
        g_name = request.data.get('gname', None)
        m_brand = request.data.get('mbrand', None)
        m_image = request.FILES.get('medimage', None)
        m_category = request.data.get('category', None)
        m_price = request.data.get('price', None)
        m_quantity = request.data.get('quantity', None)
        m_dosage = request.data.get('dosage', None)
        m_composition = request.data.get('composition', None)  # Retrieve customer ID from request data
        m_indication = request.data.get('indication', None)  # Retrieve customer ID from request data
        m_contr = request.data.get('contra', None)  # Retrieve customer ID from request data
        m_side_effects = request.data.get('side', None)  # Retrieve customer ID from request data
        m_barcode = request.data.get('barcode', None)  # Retrieve customer ID from request data
        m_supplier_id = request.data.get('supplier_id')  # Retrieve customer ID from request data

        # Check if `scid` is provided and get the corresponding customer
        if m_supplier_id:
            try:
                supplier = Suppliers.objects.get(supplier_id=m_supplier_id)
            except Suppliers.DoesNotExist:
                return JsonResponse({"status": "fail", "message": "Supplier_id not found"}, status=404)
        else:
            return JsonResponse({"status": "fail", "message": "Supplier ID not provided"}, status=400)

    
        medicine = Medicine()
        medicine.generic_name = g_name
        medicine.brand_name = m_brand
        medicine.med_image = m_image
        medicine.category = m_category
        medicine.price = m_price
        medicine.quantity = m_quantity
        medicine.dosage_form = m_dosage
        medicine.composition = m_composition
        medicine.indications = m_indication
        medicine.contraindications = m_contr
        medicine.side_effects = m_side_effects
        medicine.barcode = m_barcode
        medicine.supplier_id = supplier
        medicine.save()
        return JsonResponse({"status": "pass","medicine_id":medicine.med_id})



from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Medicine  # Make sure this import matches your app structure

class UpdateMedicine(APIView):
    def post(self, request):
        medid = request.data.get('med_id')
        med_name = request.data.get('med_name')
        med_brand = request.data.get('med_brand')
        med_category = request.data.get('med_category')
        med_price = request.data.get('med_price')
        med_quantity = request.data.get('med_quantity')
        med_dosage = request.data.get('med_dosage')
        med_created = request.data.get('med_created')
        med_updated = request.data.get('med_updated')
            # Fetch the existing Medicine object
        Medicine.objects.filter( med_id = medid, generic_name = med_name,
        brand_name = med_brand,
        category = med_category,
        price = med_price,
        quantity = med_quantity,
        dosage_form = med_dosage).update()
        request.session['med_id'] = medid
        
        return JsonResponse({"status": "success"})
        


def view_med(request):
    supplier = Suppliers()
    sid = supplier.supplier_id
    return redirect('create_med', supplier_id = sid)

def create_med(request, supplier_id):
    supplier = get_object_or_404(Suppliers, supplier_id=supplier_id)
    context = {
        "supplier_id":supplier_id,
        'currentUser':request.session['user_name'],
        'currentUserId':request.session['customer_id'], 'medId':request.session.get('med_id'),'count':request.session['count']
    }
    return render(request,  'medicine/create.html',context)


class ViewMedicines(TemplateView):
    template_name = 'medicine/medicine.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        medicine_data = Medicine.objects.all()
        customerall = Customer.objects.all()
        context = {'med_data':medicine_data, 'customer_data':customerall, 'currentUser':self.request.session['user_name'],
        'currentUserId':self.request.session['customer_id'], 'medId':self.request.session.get('med_id'),'count':self.request.session['count']}
        return context
class update():
    pass
class delete_medicine(APIView):
    def post(self, request):
        sid = request.POST['id']
        Medicine.objects.filter(med_id = sid).delete()
        return JsonResponse({"status":"pass"})
