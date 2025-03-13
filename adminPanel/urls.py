from django.urls import path
from . import views
urlpatterns = [
    path('addVendor/', views.AddSuppliers.as_view(), name='addVendor'),
    path('view_all_sellers/', views.view_all_sellers, name='view_all_sellers'),
    path('remove_vendor_admin/', views.RemoveVendorAdmin.as_view(), name='remove_vendor_admin'),
    path('update_vendor_admin/', views.update_vendor_admin, name='update_vendor_admin'),
    path('update_vendor_api/', views.UpdateVendorsAdmin.as_view(), name='update_vendor_api'),
    path('update_vendor_form/<int:id>', views.update_vendor_form, name='update_vendor_form'),
    #add medicine admin
    path('add_medicine_admin/', views.AddMedicineAdminTemplate.as_view(), name='add_medicine_admin'),
    path('add_medicine_api/', views.AddMedicineAdmin.as_view(), name='add_medicine_api'),
    path('view_medicine_admin/', views.ViewMedicineAdminTemplate.as_view(), name='view_medicine_api'),
    path('remove_medicine_api/', views.RemoveMedicineAdmin.as_view(), name='remove_medicine_api'),
]