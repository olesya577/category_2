from src.product import Product
from typing import List
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


class Category_:
    """Класс для представления категории продуктов"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products
        self.__product_count = len(products)

        # Увеличиваем счетчики класса
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> List[Product]:
        """Геттер для списка продуктов"""
        return self.products

    @property
    def product_count(self) -> int:
        """Геттер для количества продуктов в категории"""
        return len(self.products)

    def add_product(self, product: Product):
        self.products.append(product)
        Category.product_count += 1

    def __repr__(self) -> str:
        return f"Category({self.name}, {len(self.products)} products)"