from django.urls import path
from .views import medicines,create,CreateMedicine, create_med,view_med, ViewMedicines, UpdateMedicine,delete_medicine

urlpatterns = [
    path("medicines/", medicines, name='medicines'),
    path('create/', create, name='create'),
    path('create_medicine/',CreateMedicine.as_view(),name='create_medicine'),
    path('view_med', view_med, name='view_med'),
    path('dashboard/<int:supplier_id>/create' , create_med, name='create_dashboard'),
    path('view_medicine/<int:cid>/',ViewMedicines.as_view(), name='view_medicines'),
    path('update_medicines/',UpdateMedicine.as_view(),name='update_medicine'),
    path("delete_medicine/", delete_medicine.as_view(),name='delete_medicine')
]