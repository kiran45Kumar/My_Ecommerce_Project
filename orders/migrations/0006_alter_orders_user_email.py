# Generated by Django 5.1.1 on 2024-09-22 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_orders_supplier_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='user_email',
            field=models.EmailField(default='', max_length=255),
        ),
    ]
