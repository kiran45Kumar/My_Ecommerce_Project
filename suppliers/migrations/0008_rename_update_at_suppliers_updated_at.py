# Generated by Django 5.1.1 on 2024-12-12 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0007_alter_suppliers_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suppliers',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
