# Generated by Django 5.1 on 2024-10-16 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customer_first_name_alter_customer_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryPincode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.IntegerField(max_length=6)),
                ('region', models.CharField(max_length=200)),
            ],
        ),
    ]
