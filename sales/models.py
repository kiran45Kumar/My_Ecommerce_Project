from django.db import models
from medicine.models import Medicine
from customer.models import Customer
class Sales(models.Model):
    sale_id = models.AutoField(primary_key=True)
    med_id = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    quantity_sold=models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    cid = models.ForeignKey(Customer, max_length=200, on_delete=models.CASCADE)
    payment_method=models.CharField(max_length=200)
    total_amount=models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.sale_id
