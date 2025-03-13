from django.shortcuts import render
from .models import Medicine
# Create your views here.
def create(request):
    if request.method == 'POST':
        medicine_name = request.form.get('medname')
        form = Medicine(medicine_name = medicine_name)
        form.save()