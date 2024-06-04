from django.core.cache import cache

from config.settings import CACHE_ENABLED


def get_category_from_cache(model):
    """
    На вход получает данные по модели из кэша, если данных в кэше нет получаем их из БД
    """
    if CACHE_ENABLED:
        return model.objects.all()
    key = f'{model.__name__}_list'
    objects = cache.get(key)
    if objects is not None:
        return objects
    objects = model.objects.all()
    cache.set(key, objects)
    return objects
