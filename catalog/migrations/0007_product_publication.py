# Generated by Django 4.2.2 on 2024-05-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publication',
            field=models.BooleanField(default=False, verbose_name='Публикация'),
        ),
    ]
