from catalog.models import Product

def get_products_by_category(category_id):
    """ Получение списка продуктов заданной категории"""
    products = Product.objects.filter(category_id=category_id)
    if not products.exists():
        return None
    return products
