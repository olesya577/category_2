class Category:
    """Класс, который хранит информацию о категориях продуктов"""

    name: str
    description: str
    products: list
    product_count: int
    category_count: int
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        """Метод инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)
