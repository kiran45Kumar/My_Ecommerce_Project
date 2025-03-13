from django.db import models
from medicine.models import Medicine
from batches.models import Batches
class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    med_id = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    current_stock = models.IntegerField()
    reorder_level = models.IntegerField()
    storage_location=models.CharField(max_length=200)
    last_updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.inventory_id