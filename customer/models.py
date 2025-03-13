from django.db import models

class Customer(models.Model):
    ROLE_CHOICES = [
        ('admin','ADMIN'),
        ('customer','CUSTOMER'),
        ('seller','SELLER'),
        ('pharmacist','pharmasict'),
    ]
    cid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, unique=True)  
    password = models.CharField(max_length=60, null=False, blank=False)
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    role = models.CharField(max_length=100, null=True, blank=True, choices= ROLE_CHOICES) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name
class ContactForm(models.Model):
    contact_id = models.AutoField(primary_key=True)
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=50)
    contact_message = models.TextField(max_length=1000, default='')

class DeliveryPincode(models.Model):
    pincode = models.IntegerField()
    region = models.CharField(max_length=200)
    user_id = models.ForeignKey(Customer,default="", on_delete=models.CASCADE)
    def __str__(self):
        return self.pincode,self.region