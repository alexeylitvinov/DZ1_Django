import json

from django.core.management import BaseCommand

from catalog.models import Category, Product

JSON_NAME = ['catalog/fixtures/category_data.json', 'catalog/fixtures/product_data.json']


class Command(BaseCommand):
    """
    Кастомная команда на заполнение БД из сохраненных ранее .json файлов
    """
    @staticmethod
    def json_read(file_name):
        with open(file_name, encoding='utf-8') as file:
            data = json.load(file)
        return data

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_data = Command.json_read(JSON_NAME[0])
        category_for_create = []
        for i in category_data:
            category_for_create.append(
                Category(name=i['fields']['name'], description=i['fields']['description']))
        Category.objects.bulk_create(category_for_create)

        product_data = Command.json_read(JSON_NAME[-1])
        product_for_create = []
        for i in product_data:
            product_for_create.append(
                Product(name=i['fields']['name'], description=i['fields']['description'],
                        image=i['fields']['image'], price=i['fields']['price'],
                        created_at=i['fields']['created_at'], updated_at=i['fields']['updated_at'],
                        category=Category.objects.get(pk=i['fields']['category'])))
        Product.objects.bulk_create(product_for_create)
