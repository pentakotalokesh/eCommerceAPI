# Generated by Django 5.1.3 on 2025-03-22 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
        migrations.AlterModelTable(
            name='productimage',
            table='ProductImage',
        ),
        migrations.AlterModelTable(
            name='subcategory',
            table='SubCategory',
        ),
    ]
