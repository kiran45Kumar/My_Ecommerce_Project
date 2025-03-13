from django.db import models
from suppliers.models import Suppliers
from customer.models import Customer
from medicine.models import Medicine
from django.db import models
from django.utils import timezone

class Orders(models.Model):
    CHOICES = [
        ('PENDING','PENDING'),
        ('ORDERED', 'ORDERED'),
        ('SHIPPED', 'SHIPPED'),
        ('DISPATCHED', 'DISPATCHED'),
        ('DELIVERED', 'DELIVERED'),
    ]

    # Order-related fields
    order_id = models.AutoField(primary_key=True)
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # supplier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    product = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=CHOICES, default='PENDING')
    user_name = models.CharField(max_length=100,default='')
    user_phone = models.CharField(max_length=15,default='')
    user_email = models.EmailField(max_length=255,default='')
    user_address = models.TextField(default='')
    user_alternate_phone = models.CharField(max_length=15, blank=True, null=True,default='')
    user_landmark = models.CharField(max_length=255, blank=True, null=True,default='')
    user_city = models.CharField(max_length=100,default='')
    user_state = models.CharField(max_length=100,default='')
    user_postal_code = models.CharField(max_length=10,default='')
    credit_card_number = models.CharField(max_length=16, default='')
    cvv = models.CharField(max_length=3, default='111')
    expiry_date = models.CharField(max_length=7,default='222')  # Format: MM/YYYY
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id} by {self.user_name}"

class Cart(models.Model):
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.medicine.generic_name} - {self.quantity} - {self.cid}"
