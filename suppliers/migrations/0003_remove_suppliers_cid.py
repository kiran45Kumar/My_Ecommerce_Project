# Generated by Django 5.1.1 on 2024-09-07 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_suppliers_companygst'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suppliers',
            name='cid',
        ),
    ]
