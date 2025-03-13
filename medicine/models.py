from django.db import models
import PIL
from suppliers.models import Suppliers

class Medicine(models.Model):
    med_id = models.AutoField(primary_key=True)
    supplier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE, default='')
    generic_name = models.CharField(max_length=50)
    med_image = models.ImageField(default="",upload_to='uploads/')
    brand_name = models.CharField(max_length=50)
    category = models.CharField(max_length = 50)
    dosage_form = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.CharField(max_length=50)
    composition = models.CharField(max_length=50)
    indications = models.CharField(max_length=50)
    contraindications = models.CharField(max_length=50)
    side_effects = models.CharField(max_length=50)
    barcode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.generic_name