from django.urls import path
from .views import order, cart, checkout,add_to_cart,cart_page, update_cart,display,order_cart,ViewOrders,new, DeleteCart, Deleteorder,orderPlaced
urlpatterns = [
    path('order/', order, name='order'),
    path('cartn/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('add-to-cart/',add_to_cart, name='add_to_cart'),
    path('cart_page/<int:cid>/',cart_page, name='cart_page'),
    path('new/', new, name='new'),
    path('update-cart/',update_cart, name='update-cart'),
    path('display/<int:cid>/<int:med_id>/',display, name='display_orders'),
    path('order_cart/',order_cart.as_view(), name='order_cart'),
    path('view_orders/<int:cid>',ViewOrders.as_view(),name='view_orders'),
    path('delete_cart/',DeleteCart.as_view(), name="delete_cart"),
    path('delete_order/',Deleteorder.as_view(), name="delete_order"),
    path('orderPlaced/',orderPlaced, name="orderPlaced"),

]