from django.urls import path
from .views import seller, CreateSeller, delete_view,view_seller,viewallsellers,seller_dashboard,dashboard,sellerbilling,products
urlpatterns = [
    path('sell/<int:cid>', seller, name='seller_view'),
    path('dashboard/allsellers/',viewallsellers, name='allsellers'),
    path('create_seller/', CreateSeller.as_view(), name='create_seller'),
    path('view_seller/', view_seller, name='view_seller'),
    path('delete_seller/', delete_view.as_view(), name='delete_seller'),
    path('dashboard/<int:supplier_id>/suppliers', seller_dashboard, name='seller_dashboard'),
    path('dashboard/', dashboard, name='dashboard'),
    path('sellerbilling/', sellerbilling, name='sellerbilling'),
    path('products/', products, name='products'),
]