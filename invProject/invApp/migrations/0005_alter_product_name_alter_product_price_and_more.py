# Generated by Django 5.1.1 on 2024-09-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invApp', '0004_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.CharField(max_length=255),
        ),
    ]
