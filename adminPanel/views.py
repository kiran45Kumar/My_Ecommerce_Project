from django.shortcuts import render
from suppliers.models import Suppliers
from django.views.generic import TemplateView
from rest_framework.views import APIView
from django.http import JsonResponse
from medicine.models import Medicine
# Create your views here.
class AddSuppliers(APIView):
    def post(self, request):
        supplier_name = request.POST.get('supplier_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        CompanyName = request.POST.get('CompanyName')
        CompanyGst = request.POST.get('CompanyGst')
        address = request.POST.get('address')
        suppliers  = Suppliers()
        suppliers.supplier_name = supplier_name
        suppliers.phone_number = phone_number
        suppliers.email = email
        suppliers.CompanyName = CompanyName
        suppliers.CompanyGst = CompanyGst
        suppliers.account_created_by = 'Admin'        
        suppliers.address = address        
        suppliers.save()
        return JsonResponse({"status":"pass"})
    
class UpdateVendorsAdmin(APIView):
    def post(self, request):
        id = request.POST.get('id')
        supplier_name = request.POST.get('supplier_name')
        phone_number = request.POST.get('supplier_phone')
        email = request.POST.get('supplier_email')
        CompanyName = request.POST.get('CompanyName')
        CompanyGst = request.POST.get('CompanyGst')
        address = request.POST.get('supplier_address')
        account_created_by = request.POST.get('account_created_by')
        Suppliers.objects.filter(supplier_id = id).update(
        supplier_name = supplier_name,
        phone_number = phone_number,
        email = email,
        CompanyName = CompanyName,
        CompanyGst = CompanyGst,     
        address = address,
        account_created_by = account_created_by,
        )
        return JsonResponse({"status":"pass"})
    
class RemoveVendorAdmin(APIView):
    def post(self, request):
        id = request.POST.get('id')
        Suppliers.objects.filter(supplier_id = id).delete()
        return JsonResponse({"status":"pass"})
def view_all_sellers(request):
    sellers = Suppliers.objects.all().order_by('-created_at')
    return render(request, 'admin/table.html',{'sellers':sellers} )
def update_vendor_admin(request):
    sellers = Suppliers.objects.all().order_by('-created_at')
    return render(request, 'admin/update_vendor.html',{'sellers':sellers} )
def update_vendor_form(request,id):
    seller = Suppliers.objects.get(supplier_id = id)
    return render(request, 'admin/update_vendor_form.html',{'seller':seller} )
class AddMedicineAdmin(APIView):
    def post(self, request):
        generic_name = request.POST.get('generic_name')
        med_image = request.FILES.get('med_image')
        brand_name = request.POST.get('brand_name')
        category = request.POST.get('category')
        dosage_form = request.POST.get('dosage_form')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        composition = request.POST.get('composition')
        indications = request.POST.get('Indications')
        contraindications = request.POST.get('contraindications')
        side_effects = request.POST.get('side_effects')
        supplier_id = request.POST.get('supplier_vendor')
        barcode = request.POST.get('barcode')
        supplier = Suppliers.objects.get(supplier_id = supplier_id)
        medicines = Medicine()
        medicines.generic_name = generic_name
        medicines.med_image = med_image
        medicines.brand_name = brand_name
        medicines.category = category
        medicines.dosage_form = dosage_form
        medicines.price = price
        medicines.quantity = quantity
        medicines.composition = composition
        medicines.indications = indications
        medicines.contraindications = contraindications
        medicines.side_effects =  side_effects
        medicines.supplier_id = supplier
        medicines.barcode = barcode
        medicines.save()
        return JsonResponse({"status":"pass"})
class AddMedicineAdminTemplate(TemplateView):
    template_name = "admin/add_medicine_admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        suppliers = Suppliers.objects.all()
        context['suppliers'] = suppliers
        return context
class ViewMedicineAdminTemplate(TemplateView):
    template_name = "admin/view_medicine_admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        medicines = Medicine.objects.all()
        context['medicines'] = medicines
        return context
class RemoveMedicineAdmin(APIView):
    def post(self, request):
        id = request.POST.get('id')
        Medicine.objects.filter(med_id = id).delete()
        return JsonResponse({"status":"pass"})