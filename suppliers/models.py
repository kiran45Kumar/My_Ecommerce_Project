from django.db import models
from customer.models import Customer


class Suppliers(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=200)
    phone_number=models.IntegerField()
    email = models.EmailField(unique=True,default='')
    CompanyName = models.CharField(max_length=200, default='')
    CompanyGst = models.CharField(max_length=200, default='')
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    address=models.CharField(max_length=200)
    account_created_by = models.CharField(max_length=20, default="", null=True, blank=True)
    rating=models.CharField(max_length=200,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.supplier_id
