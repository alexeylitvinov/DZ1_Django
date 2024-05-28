# Generated by Django 4.2.2 on 2024-05-28 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_publication', 'Can edit publication'), ('can_edit_description', 'Can edit description'), ('can_edit_category', 'Can edit category')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]