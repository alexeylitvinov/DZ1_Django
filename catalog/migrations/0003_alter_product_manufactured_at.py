# Generated by Django 5.0.4 on 2024-04-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_manufactured_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufactured_at',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Дата производства'),
        ),
    ]